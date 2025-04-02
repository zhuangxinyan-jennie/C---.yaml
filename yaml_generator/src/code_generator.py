import yaml # type: ignore

# 生成YAML配置
class YAMLGenerator:
    def __init__(self, analyzer):
        self.analyzer = analyzer
        # 初始化生成器，接收一个分析器
    def generate_config(self):
        config = {
            'top': [self.analyzer.functions[0]] if self.analyzer.functions else [],
            'funcList': self.analyzer.functions,
            'loopConfig': self._generate_loop_configs(),
            'arrList': [],
            'interList': []#接口列表,当前为空
        }
        return yaml.dump(config, sort_keys=False)
        

    # 生成循环配置
    def _generate_loop_configs(self):
        configs = []
        # 遍历循环列表
        for i, loop in enumerate(self.analyzer.loops, 1):
            config = {
                f'group{i}': {
                    'level': loop['depth'],#循环深度
                    'unroll': 'off',#不展开，默认关闭
                    'pipeline': 'off',#不流水，默认关闭
                    'flatten': 'off'#不展平，默认关闭
                }
            }
            configs.append(config)
        return configs