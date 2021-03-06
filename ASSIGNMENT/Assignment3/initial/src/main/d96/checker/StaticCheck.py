
#ID: 1914659
from AST import *
from Visitor import *
from StaticError import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):

        return "MType([" + ','.join(str(i) for i in self.partype) + "]" + ', ' + str(self.rettype) + ")"


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype)+"," + str(self.value) + ' )'


class ExpUtils:
    @staticmethod
    def isNaNType(expType):
        return type(expType) not in [IntType, FloatType]

    @staticmethod
    def checkCoerce(lhsType, expType):

        if(type(lhsType) is not type(expType)):
            if(not(not(ExpUtils.isNaNType(expType)) and (type(lhsType) is FloatType))):
                return False

        return True


class StaticChecker(BaseVisitor):

    global_envi = [
        # Symbol("getInt", MType([], IntType())),
        # Symbol("putIntLn", MType([IntType()], VoidType()))
    ]
    # global_envi = []

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def returnType(self, lhs, exp):
        typeLhs = lhs
        typeExp = exp
        if type(lhs) is Symbol:
            typeLhs = (None, lhs.mtype, True if type(
                lhs.value) is Constant else False)
        if type(exp) is Symbol:
            typeExp = (None, exp.mtype, True if type(
                exp.value) is Constant else False)

        return (typeLhs, typeExp)

    def returnTypeOne(self, lhs):
        typeLhs = lhs
        if type(lhs) is Symbol:
            typeLhs = (None, lhs.mtype, True if type(
                lhs.value) is Constant else False)

        return typeLhs

    def lookup(self, name, lst, func):
        for x in lst:
            if name == func(x):
                return x
        return None

    def convertToSymbol(self, decl, returnType=None):

        # Function convert declare to Symbol
        if isinstance(decl, AttributeDecl):
            if type(decl.decl) is ConstDecl:
                return Symbol(decl.decl.constant.name, decl.decl.constType, (Constant(), decl.kind))
            else:
                return Symbol(decl.decl.variable.name, decl.decl.varType, (Variable(), decl.kind))
        elif type(decl) is ConstDecl:
            return Symbol(decl.constant.name, decl.constType, Constant())
        elif type(decl) is VarDecl:
            if type(decl.varType) is Class:
                return Symbol(decl.variable.name, decl.varType, decl.varType.classname.name)
            return Symbol(decl.variable.name, decl.varType, Variable())

        elif isinstance(decl, MethodDecl):
            return Symbol(decl.name.name, MType([x.varType for x in decl.param], returnType))

    def checkClassDefined(self, list_class, name):
        res = self.lookup(name, list_class, lambda x: x.name)
        if res is not None:
            return True
        return False

    def checkAttClass(self, list_class, name, attName, kind, returnType=None):
        res = self.lookup(name, list_class, lambda x: x.name)
        if res is not None:
            for x in res.mtype:
                if x.name == attName:
                    return x
        return None

    def checkEntryPoint(self, global_class):
        res = self.lookup("Program", global_class, lambda x: x.name)
        if res is not None:
            for x in res.mtype:
                if x.name == 'main' and (type(x.mtype) is MType):
                    if x.mtype.partype == []:
                        return True
        return False

    def checkParamArgu(self, ast,  checked, c):
        listType = []
        for x in ast.param:
            listType += [self.visit(x, c)[1]]
        if len(listType) is not len(checked.mtype.partype):
            raise TypeMismatchInStatement(ast)
        for i in range(0, max(len(listType), len(checked.mtype.partype))):
            if not ExpUtils.checkCoerce(checked.mtype.partype[i], listType[i]):
                raise TypeMismatchInStatement(ast)
        return

    def visitProgram(self, ast, global_envi):
        global_envi = global_envi[:]
        for x in ast.decl:
            global_envi += [self.visit(x, global_envi)]

        # check Entry Point
        if(not self.checkEntryPoint(global_envi)):
            raise NoEntryPoint()

        return []

    def visitClassDecl(self, ast, global_envi):
        res = self.lookup(ast.classname.name, global_envi, lambda x: x.name)

        if res is not None:
            raise Redeclared(Class(), ast.classname.name)

        if ast.parentname:
            parent = self.lookup(
                ast.parentname.name, global_envi, lambda x: x.name)
            if parent is None:
                raise Undeclared(Class(), ast.parentname.name)
        local_evi = []
        # self.toListSym(ast.memlist, local_evi)

        for x in ast.memlist:
            local_evi += [self.visit(x, (global_envi, local_evi))]

        return Symbol(ast.classname.name, local_evi, Class())

    def visitAttributeDecl(self, ast, c):
        local_envi = c[1]
        sym = self.convertToSymbol(ast)
        res = self.lookup(sym.name, local_envi, lambda x: x.name)

        if res is None:
            self.visit(ast.decl, (c[0], c[1], [], []))
            return sym
        else:
            raise Redeclared(Attribute(), sym.name)

        # return self.visit(ast.decl, local_envi)

        # is_redeclare = self.lookup(ast.constant, local_envi, lambda x: x.name)
        # if is_redeclare:
        #     raise Redeclared(Constant(), ast.constant.name)

        # return Symbol(ast.constant, MType(None, ast.constType))

    def visitMethodDecl(self, ast, c):
        global_class = c[0]
        global_envi = c[1]
        is_in_loop = False

        res = self.lookup(ast.name.name, global_envi,
                          lambda x: x.name if type(x.mtype) is MType else None)

        # check param of method
        list_param = []
        for x in ast.param:
            list_param.extend(self.visit(x, (list_param, 'para')))

        # check body of method
        returnType = self.visit(
            ast.body, (global_class, global_envi, [], list_param, is_in_loop))

        if res is not None:
            raise Redeclared(Method(), ast.name.name)
        sym = self.convertToSymbol(ast, returnType)
        # print(returnType)
        # print(sym)
        return sym

    def visitVarDecl(self, ast, c):
        kind = global_class = global_envi = local_envi = None
        if c[1] == 'para':
            kind = c[1]
            block_scope = c[0]
        else:
            kind = None
            global_class = c[0]
            global_envi = c[1]
            local_envi = c[2]
            block_scope = c[3]

        sym = self.convertToSymbol(ast)

        # check declared variable
        res = self.lookup(sym.name,  block_scope,
                          lambda x: x.name if type(x.mtype) is not MType else None)

        if ast.varInit:
            # Check TypeMismatchInConstant
            c1 = c
            if type(ast.varInit) is ArrayLiteral:
                if type(ast.varType) is not ArrayType:
                    raise TypeMismatchInConstant(ast)
                c1 = c + (ast.varType,)

            typExpr = self.returnTypeOne(self.visit(ast.varInit, c1))
            if not ExpUtils.checkCoerce(ast.varType, typExpr[1]) and (typExpr[1] is not None):
                raise TypeMismatchInConstant(ast)

            # check size arr
            if(type(typExpr[1]) is ArrayType):
                if int(typExpr[1].size) is not int(ast.varType.size) or not ExpUtils.checkCoerce(ast.varType.eleType, typExpr[1].eleType):
                    raise TypeMismatchInConstant(ast)
            elif type(typExpr[1]) is ClassType and type(ast.varType) is ClassType:
                if(typExpr[1].classname.name !=
                   ast.varType.classname.name):
                    raise TypeMismatchInConstant(ast)

        if type(ast.varType) is ClassType:
            nameClass = self.visit(ast.varType, local_envi)
            checked = self.checkClassDefined(
                global_class, nameClass)
            if not checked:
                raise Undeclared(Class(), nameClass)

        if res is not None:
            if kind == 'para':
                raise Redeclared(Parameter(), sym.name)
            else:
                raise Redeclared(Variable(), sym.name)

        # if ast.varInit:
        #     # Check TypeMismatchInConstant
        #     c1 = c
        #     if type(ast.varInit) is ArrayLiteral:
        #         c1 = c + (ast.varType,)

        #     typExpr = self.returnTypeOne(self.visit(ast.varInit, c1))
        #     if not ExpUtils.checkCoerce(ast.varType, typExpr[1]):
        #         raise TypeMismatchInConstant(ast)

        #     # check size arr
        #     if(type(typExpr[1]) is ArrayType):
        #         if int(typExpr[1].size) is not int(ast.varType.size):
        #             raise TypeMismatchInConstant(ast)
        #     elif type(typExpr[1]) is ClassType and type(ast.varType) is ClassType:
        #         if(typExpr[1].classname.name !=
        #            ast.varType.classname.name):
        #             raise TypeMismatchInConstant(ast)

        return [sym]

    def visitConstDecl(self, ast, c):
        global_class, global_envi, local_envi, block_scope = c[0], c[1], c[2], c[3]
        sym = self.convertToSymbol(ast)

        # check declared variable
        res = self.lookup(sym.name, block_scope,
                          lambda x: x.name if type(x.mtype) is not MType else None)

        if type(ast.constType) is ClassType:
            nameClass = self.visit(ast.constType, local_envi)

            checked = self.checkClassDefined(
                global_class, nameClass)
            if not checked:
                raise Undeclared(Class(), nameClass)

        if res is not None:
            raise Redeclared(Constant(), sym.name)

        # Check TypeMismatchInConstant
        if ast.value:
            c1 = c
            if type(ast.value) is ArrayLiteral:
                if type(ast.constType) is not ArrayType:
                    c1 = c + (ast.constType,)
            typExpr = self.returnTypeOne(self.visit(ast.value, c1))
            if not ExpUtils.checkCoerce(ast.constType, typExpr[1]) and (typExpr[1] is not None):
                raise TypeMismatchInConstant(ast)

            # check size arr
            if(type(typExpr[1]) is ArrayType):
                if int(typExpr[1].size) is not int(ast.constType.size) or not ExpUtils.checkCoerce(ast.varType.eleType, typExpr[1].eleType):
                    raise TypeMismatchInConstant(ast)
            elif type(typExpr[1]) is ClassType and type(ast.constType) is ClassType:
                if(typExpr[1].classname.name !=
                   ast.constType.classname.name):
                    raise TypeMismatchInConstant(ast)

            if typExpr[2] is not True:
                raise IllegalConstantExpression(ast.value)
        else:
            raise IllegalConstantExpression(None)

        return [sym]

    def visitBlock(self, ast, c):
        global_class = c[0]
        global_envi = c[1]
        local_envi = c[2]
        block_scope = c[3]
        is_in_loop = c[4]
        returnType = None

        # check redecl
        for x in ast.inst:
            if type(x) is Block:
                self.visit(x, (global_class, global_envi,
                           local_envi + block_scope, [], is_in_loop))
            else:
                decl = self.visit(
                    x, (global_class, global_envi, local_envi, block_scope, is_in_loop))
                if type(decl) is list:
                    if type(decl[0]) is Symbol:
                        block_scope.extend(decl)
                elif type(x) is Return:

                    # check break, continue

                    if((returnType is not decl) and ((type(returnType) is FloatType)
                                                     or (type(decl) is FloatType))):
                        decl = FloatType()
                    elif returnType is not decl and returnType is not None:
                        raise TypeMismatchInStatement(x)
                    returnType = decl

        # return voidtype if not return any
        if returnType is None:
            returnType = VoidType()
        # local_envi.extend(block_scope)
        return returnType

    def visitAssign(self, ast, c):

        lhs = self.visit(ast.lhs, c)

        # check assign constant
        if type(lhs.value) is Constant:
            raise CannotAssignToConstant(ast)
        # check size in array
        if type(ast.exp) is ArrayLiteral:
            if type(lhs.mtype) is not ArrayType:
                raise TypeMismatchInStatement(ast)
            c = c + (lhs.mtype,)
            exp = self.visit(ast.exp, c)

            if (int(exp[1].size) is not int(lhs.mtype.size) or not(ExpUtils.checkCoerce(lhs.mtype.eleType, exp[1].eleType))):
                raise TypeMismatchInStatement(ast)

        else:
            exp = self.visit(ast.exp, c)

        # check mis match
        typeLhs,  typeExp = self.returnType(lhs, exp)
        if not ExpUtils.checkCoerce(typeLhs[1], typeExp[1]):
            raise TypeMismatchInStatement(ast)

        return

    def visitFieldAccess(self, ast, c):
        global_class = c[0]
        global_envi = c[1]
        local_envi = c[2]
        block_scope = c[3]
        checked = None
        is_constant = False
        if type(ast.obj) is SelfLiteral:
            checked = self.lookup(ast.fieldname.name, global_envi, lambda x: x.name if type(
                x.mtype) is not MType else None)
        else:
            # Check method of class

            sym = self.lookup(ast.obj.name, local_envi +
                              block_scope, lambda x: x.name)
            if not sym:
                # check Illegal Member Access
                symClass = self.lookup(
                    ast.obj.name, global_class, lambda x: x.name)
                if symClass:
                    raise IllegalMemberAccess(ast)
                raise Undeclared(Class(), ast.obj.name)
            elif (sym and type(sym.mtype) is not ClassType):
                raise TypeMismatchInExpression(ast)
            else:
                checked = self.checkAttClass(
                    global_class, sym.mtype.classname.name, ast.fieldname.name, Attribute())

        # For an attribute access E.id, E must be in class type.
        if not checked:
            raise Undeclared(Attribute(), ast.fieldname.name)

        if isinstance(checked.value[1], Constant):
            is_constant = True

        return checked

    def visitIf(self, ast, c):
        global_class, global_envi, local_envi, block_scope, is_in_loop = c

        is_boolean = self.visit(
            ast.expr, c)
        then_stmt = self.visit(
            ast.thenStmt, (global_class, global_envi, local_envi + block_scope, [], is_in_loop))

        if ast.elseStmt:
            elseStmt = self.visit(
                ast.elseStmt, (global_class, global_envi, local_envi + block_scope, [], is_in_loop))
        if type(is_boolean[1]) is not BoolType:
            raise TypeMismatchInStatement(ast)
        return

    def visitFor(self, ast, c):
        id = self.visit(ast.id, c)
        if type(id.value) is Constant:
            raise CannotAssignToConstant(Assign(ast.id, ast.expr1))
        elif type(id.mtype) is not IntType:
            raise TypeMismatchInStatement(Assign(ast.id, ast.expr1))

        expr1 = self.visit(ast.expr1, c)
        expr2 = self.visit(ast.expr2, c)
        expr3 = self.visit(ast.expr3, c)
        typeExpr1, typeExpr2 = self.returnType(expr1, expr2)
        typeExpr3 = self.returnTypeOne(expr3)
        is_in_loop = True

        if not(isinstance(typeExpr1[1], IntType) and isinstance(typeExpr2[1], IntType) and isinstance(typeExpr3[1], IntType)):
            raise TypeMismatchInStatement(ast)

        loop = self.visit(ast.loop, (c[0], c[1], c[2] + c[3], [], is_in_loop))
        return

    def visitBinaryOp(self, ast, c):
        left = self.visit(ast.left, c)
        right = self.visit(ast.right, c)

        typeLeft, typeRight = self.returnType(left, right)
        # check Arithmetic operators
        if ast.op in ['-', '+', '*', '/']:

            if (type(typeLeft[1]) not in [IntType, FloatType] or type(typeRight[1]) not in [IntType, FloatType]):
                raise TypeMismatchInExpression(ast)
            elif isinstance(typeLeft[1], FloatType) or isinstance(typeRight[1], FloatType):
                typBi = FloatType()
            else:
                if ast.op == '/':
                    typBi = FloatType
                else:
                    typBi = IntType()

        elif ast.op == '%':
            if not isinstance(typeLeft[1], IntType) or not isinstance(typeRight[1], IntType):
                raise TypeMismatchInExpression(ast)
            typBi = IntType()

        # check  Boolean operators
        if ast.op in ['&&', '||']:

            if not(isinstance(typeLeft[1], BoolType) and isinstance(typeRight[1], BoolType)):
                raise TypeMismatchInExpression(ast)
            typBi = BoolType()
        elif ast.op == '==.':
            if not(isinstance(typeLeft[1], StringType) and isinstance(typeRight[1], StringType)):
                raise TypeMismatchInExpression(ast)
            typBi = BoolType()

        # check Relational operators
        if ast.op == '+.':

            if not(isinstance(typeLeft[1], StringType) or isinstance(typeRight[1], StringType)):
                raise TypeMismatchInExpression(ast)
            typBi = StringType()

        # check Relational operators

        if ast.op in ['==', '!=']:
            if(not((isinstance(typeLeft[1], BoolType) or isinstance(typeLeft[1], IntType)) and (isinstance(typeRight[1], BoolType) or isinstance(typeRight[1], IntType)))):
                raise TypeMismatchInExpression(ast)
            typBi = BoolType()
        elif ast.op in ['<', '>', '<=', '>=']:
            if(not((isinstance(typeLeft[1], FloatType) or isinstance(typeLeft[1], IntType)) and (isinstance(typeRight[1], FloatType) or isinstance(typeRight[1], IntType)))):
                raise TypeMismatchInExpression(ast)
            typBi = BoolType()

        is_constant = typeLeft[2] and typeRight[2]

        return (None, typBi, is_constant)

    def visitUnaryOp(self, ast, c):
        typeBody = self.returnTypeOne(self.visit(ast.body, c))
        if ast.op == '-':
            if not(isinstance(typeBody[1], IntType) or isinstance(typeBody, FloatType)):
                raise TypeMismatchInExpression(ast)
        elif ast.op == '!':
            if not isinstance(typeBody[1], BoolType):
                raise TypeMismatchInExpression(ast)
        return typeBody

    def visitId(self, ast, c):
        # all decl to check declared or not
        list_decl = c[1] + c[2] + c[3]
        res = self.lookup(ast.name, list_decl, lambda x: x.name if type(
            x.mtype) is not MType else None)

        if res is None:
            raise Undeclared(Identifier(), ast.name)

        # if type(res.value) is Constant:
        #     raise CannotAssignToConstant(as)
        return res

    def visitArrayCell(self, ast, c):
        arr = self.visit(ast.arr, c)
        typeArr = arr.mtype

        for x in ast.idx:
            typeIdx = self.returnTypeOne(self.visit(x, c))

            if type(typeIdx[1]) is not IntType:
                raise TypeMismatchInExpression(ast)

        if type(typeArr) is not ArrayType:
            raise TypeMismatchInExpression(ast)

        return Symbol(None, typeArr.eleType, arr.value)

    def visitIntLiteral(self, ast, c):
        return (None, IntType(), True)

    def visitFloatLiteral(self, ast, c):
        return (None, FloatType(), True)

    def visitBooleanLiteral(self, ast, c):
        return (None, BoolType(), True)

    def visitStringLiteral(self, ast, c):
        return(None, StringType(), True)

    def visitClassType(self, ast, c):
        return ast.classname.name

    def visitArrayType(self, ast, c):
        return

    def visitCallExpr(self, ast, c):

        global_class, global_envi, local_envi, block_scope = c[0], c[1], c[2], c[3]
        checked = None
        if type(ast.obj) is SelfLiteral:
            checked = self.lookup(ast.method.name, global_envi, lambda x: x.name if type(
                x.mtype) is MType else None)
        else:
            # Check method of class

            sym = self.lookup(ast.obj.name, local_envi +
                              block_scope, lambda x: x.name)
            if not sym:
                # check Illegal Member Access
                symClass = self.lookup(
                    ast.obj.name, global_class, lambda x: x.name)
                if symClass:
                    raise IllegalMemberAccess(ast)
                raise Undeclared(Class(), ast.obj.name)
                raise Undeclared(Class(), ast.obj.name)
            elif (sym and type(sym.mtype) is not ClassType):

                raise TypeMismatchInStatement(ast)
            else:
                checked = self.checkAttClass(
                    global_class, sym.mtype.classname.name, ast.method.name, Method())

        if not checked:
            raise Undeclared(Method(), ast.method.name)
        else:
            # check parameter and argument
            self.checkParamArgu(ast, checked, c)

            # check Return Type
            if(type(checked.mtype.rettype) is VoidType):
                raise TypeMismatchInStatement(ast)

        return checked.mtype.rettype

    def visitCallStmt(self, ast, c):
        global_class = c[0]
        global_envi = c[1]
        local_envi = c[2]
        block_scope = c[3]
        checked = None
        if type(ast.obj) is SelfLiteral:
            checked = self.lookup(ast.method.name, global_envi, lambda x: x.name if type(
                x.mtype) is MType else None)
        else:
            # Check method of class

            sym = self.lookup(ast.obj.name, local_envi +
                              block_scope, lambda x: x.name)
            if not sym:
                # check Illegal Member Access
                symClass = self.lookup(
                    ast.obj.name, global_class, lambda x: x.name)
                if symClass:
                    raise IllegalMemberAccess(ast)
                raise Undeclared(Class(), ast.obj.name)
                raise Undeclared(Class(), ast.obj.name)
            elif (sym and type(sym.mtype) is not ClassType):

                raise TypeMismatchInStatement(ast)
            else:
                checked = self.checkAttClass(
                    global_class, sym.mtype.classname.name, ast.method.name, Method())

        if not checked:
            raise Undeclared(Method(), ast.method.name)
        else:
            # check parameter and argument
            self.checkParamArgu(ast, checked, c)

            # check return Type
            if (type(checked.mtype.rettype) is not VoidType):
                raise TypeMismatchInStatement(ast)

        return

    def visitReturn(self, ast, c):
        returnType = self.visit(ast.expr, c)
        if not returnType:
            return VoidType()
        return returnType

    def visitBreak(self, ast, c):
        is_in_loop = c[4]
        if is_in_loop == False:
            raise MustInLoop(ast)

    def visitContinue(self, ast, c):
        is_in_loop = c[4]
        if is_in_loop == False:
            raise MustInLoop(ast)

    def visitNewExpr(self, ast, c):
        res = self.lookup(ast.classname.name, c[0], lambda x: x.name)
        if res is None:
            raise Undeclared(Class(), ast.classname.name)
        checked = self.checkAttClass(
            c[0], ast.classname.name, "Constructor", Method())
        if checked is None:
            checked = Symbol("Constructor", MType([], VoidType()), None)

        # check parameter and argument
        self.checkParamArgu(ast, checked, c)

        return (None, ClassType(Id(ast.classname.name)), True)
        # return (ast.classname.name, ClassType(), True)

    def visitArrayLiteral(self, ast, c):
        size = len(ast.value)
        typeArr = c[-1].eleType
        typeEle = self.visit(ast.value[0], c[:-1])
        for x in ast.value[1:]:
            typeX = self.visit(x, c[:-1])
            if type(typeEle[1]) is not type(typeX[1]):
                raise IllegalArrayLiteral(ast)

        return (None, ArrayType(size, typeEle[1]), True)

    def visitNullLiteral(self, ast, c):
        return (None, None, None)
