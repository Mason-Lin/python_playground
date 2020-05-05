from pathlib import Path
import astunparse
import ast

here = Path(__file__).absolute()
filename = Path(here.parent, 'simple_fun.py')
func_def = open(filename).read()
# print(func_def)

# create code object
cm = compile(func_def, filename, 'exec')
print(cm, type(cm))
exec(cm)

# create ast
r_node = ast.parse(func_def)
print(r_node, type(r_node))

print(astunparse.dump(r_node))
print(astunparse.unparse(r_node))


# modify code by ast, replace add with sub
class CodeVisitor(ast.NodeVisitor):
    def visit_BinOp(self, node):
        if isinstance(node.op, ast.Add):

            node.op = ast.Sub()
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        print('Function Name:%s' % node.name)
        self.generic_visit(node)
        # func_log_stmt = ast.Print(
        #     dest = None,
        #     values = [ast.Str(s = 'calling func: %s' % node.name, lineno = 0, col_offset = 0)],
        #     nl = True,
        #     lineno = 0,
        #     col_offset = 0,
        # )
        # node.body.insert(0, func_log_stmt)


r_node = ast.parse(func_def)
visitor = CodeVisitor()
visitor.visit(r_node)
# print astunparse.dump(r_node)
print(astunparse.unparse(r_node))
exec(compile(r_node, '<string>', 'exec'))


# modify the whole code
print('===================================================')
class CodeTransformer(ast.NodeTransformer):
    def visit_BinOp(self, node):
        if isinstance(node.op, ast.Add):
            node.op = ast.Sub()
        self.generic_visit(node)
        return node

    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        if node.name == 'add':
            node.name = 'sub'
        args_num = len(node.args.args)

        # mason add
        replace = {'add': 'sub', 'x': 'a', 'y': 'b'}
        for arg in node.args.args:
            re_id = replace.get(arg.arg, None)
            arg.arg = re_id or arg.arg

        args = tuple([arg.arg for arg in node.args.args])
        func_log_stmt = ''.join([f'print("calling func: {node.name}, args: {args}")'])
        node.body.insert(0, ast.parse(func_log_stmt))
        return node

    def visit_Name(self, node):
        replace = {'add': 'sub', 'x': 'a', 'y': 'b'}
        re_id = replace.get(node.id, None)
        node.id = re_id or node.id
        print(node.id)
        self.generic_visit(node)
        return node


r_node = ast.parse(func_def)
transformer = CodeTransformer()
r_node = transformer.visit(r_node)
# print astunparse.dump(r_node)
source = astunparse.unparse(r_node)
print(source)
# exec compile(r_node, '<string>', 'exec')        # 新加入的node func_log_stmt 缺少lineno和col_offset属性
exec(compile(source, '<string>', 'exec'))
exec(compile(ast.parse(source), '<string>', 'exec'))


