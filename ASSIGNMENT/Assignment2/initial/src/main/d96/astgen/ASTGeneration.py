from AST import *
from D96Parser import D96Parser
from D96Visitor import D96Visitor


class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        return Program([self.visit(x) for x in ctx.class_decl()])
    
    def visitClass_decl(self, ctx: D96Parser.Class_declContext):
        mem_decl_list = []
        if ctx.COL(): 
            if ctx.mem_decl():
               return ClassDecl(Id(ctx.IDEN(0).getText()), [self.visit(x) for x in ctx.mem_decl()]), Id(ctx.IDEN(1).getText())
            return ClassDecl(Id(ctx.IDEN(0).getText()), [], Id(ctx.IDEN(1).getText()))
        if ctx.mem_decl():
            [ mem_decl_list.extend(self.visit(x)) for x in ctx.mem_decl()]
            return ClassDecl(Id(ctx.IDEN(0).getText()), mem_decl_list)
        return ClassDecl(Id(ctx.IDEN(0).getText()), [])

    def visitMem_decl(self, ctx: D96Parser.Mem_declContext):
        if ctx.attr_decl():
            return self.visit(ctx.attr_decl())
        if ctx.func_decl():
            return self.visit(ctx.method_decl())

    def visitAttr_decl(self, ctx: D96Parser.Attr_declContext):
        if ctx.immutable_attr():
            return self.visit(ctx.immutable_attr())
        return self.visit(ctx.mutable_attr())
    
    def visitImmutable_attr(self, ctx: D96Parser.Immutable_attrContext):
        IdListType = self.visit(ctx.id_list_type())
        return [AttributeDecl(Static(), ConstDecl(id, dataType)) for (id, dataType) in IdListType] 
    
    def visitId_list_type(self, ctx: D96Parser.Id_list_typeContext):
        dataType = self.visit(ctx.data_type())
        idList = self.visit(ctx.id_list())
        return [(id, dataType) for id in idList]
    
    def visitData_type(self, ctx: D96Parser.Data_typeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BoolType()
        
    def visitId_list(self, ctx: D96Parser.Id_listContext):
        return [self.visit(iden_dol) for iden_dol in ctx.iden_dol()]
    
    def visitIden_dol(self, ctx: D96Parser.Iden_dolContext):
            return Id(ctx.IDEN().getText())
    # def visitProgram(self, ctx: D96Parser.ProgramContext):
    #     return Program([FuncDecl(Id("main"),
    #                              [],
    #                              self.visit(ctx.mptype()),
    #                              Block([], [self.visit(ctx.body())] if ctx.body() else []))])

    # def visitMptype(self, ctx: D96Parser.MptypeContext):
    #     if ctx.INTTYPE():
    #         return IntType()
    #     else:
    #         return VoidType()

    # def visitBody(self, ctx: D96Parser.BodyContext):
    #     return self.visit(ctx.funcall())

    # def visitFuncall(self, ctx: D96Parser.FuncallContext):
    #     return CallExpr(Id(ctx.ID().getText()), [self.visit(ctx.exp())] if ctx.exp() else [])

    # def visitExp(self, ctx: D96Parser.ExpContext):
    #     if (ctx.funcall()):
    #         return self.visit(ctx.funcall())
    #     else:
    #         return IntLiteral(int(ctx.INTLIT().getText()))