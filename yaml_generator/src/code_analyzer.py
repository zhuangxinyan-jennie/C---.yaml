from pycparser import c_ast # type: ignore

# 代码分析器，分析C的抽象语法树AST
class CodeAnalyzer:
    def __init__(self, ast):
        #初始化函数，接收一个抽象语法树AST
        self.ast = ast
        #初始化函数列表，循环列表，数组列表，接口列表
        self.functions = []
        self.loops = []
        self.arrays = []
        self.interfaces = []
        
    def analyze(self):
        #如果抽象语法树AST为空，则返回
        if self.ast is None:
            return
            
        # 函数访问器，继承自c_ast.NodeVisitor
        class FuncVisitor(c_ast.NodeVisitor):
            def __init__(self):
                self.functions = []#查找收集函数名
                
            def visit_FuncDef(self, node):
                self.functions.append(node.decl.name)# 添加函数名
                
        # 循环访问器，继承自c_ast.NodeVisitor，查找收集循环
        class LoopVisitor(c_ast.NodeVisitor ):
            def __init__(self):
                self.loops = []#查找收集循环
                self.current_depth = 0#当前深度
                
            def visit_For(self, node):
                self.current_depth += 1#当前深度加1
                self.loops.append({
                    'depth': self.current_depth,
                    'type': 'for'#记录循环类型为for
                })
                self.generic_visit(node)#继续访问子节点
                self.current_depth -= 1#离开循环时当前深度减1
                
        # 创建函数访问器和循环访问器
        func_visitor = FuncVisitor()
        func_visitor.visit(self.ast)#访问抽象语法树，遍历AST查找函数
        self.functions = func_visitor.functions#保存找到的函数
        
        loop_visitor = LoopVisitor()
        loop_visitor.visit(self.ast)#访问抽象语法树，遍历AST查找循环
        self.loops = loop_visitor.loops#保存找到的循环
        
        # 创建数组访问器，查找收集数组
        class ArrayVisitor(c_ast.NodeVisitor):
            def __init__(self):
                self.arrays = []
