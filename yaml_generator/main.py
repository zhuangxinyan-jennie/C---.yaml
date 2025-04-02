#-*- coding: utf-8 -*-
from src.code_parser import CodeParser
from src.code_analyzer import CodeAnalyzer
from src.code_generator import YAMLGenerator

def main():
    # 初始化解析器
    parser = CodeParser()
    
    # 读取C代码文件
    input_file = 'examples/input.c'
    ast = parser.parse_file(input_file)
    
    if ast is None:
        print("解析失败")
        return
        
    # 分析代码
    analyzer = CodeAnalyzer(ast)
    analyzer.analyze()
    
    # 生成YAML配置
    generator = YAMLGenerator(analyzer)
    yaml_config = generator.generate_config()
    
    # 保存配置文件
    output_file = 'output.yaml'
    with open(output_file, 'w') as f:
        f.write(yaml_config)
    
    print(f"配置文件已生成: {output_file}")

if __name__ == "__main__":
    main()