from django.contrib import admin

# Register your models here.
from .models import Grades,Students,Articles

# 关联对象
class StudentsInfo(admin.TabularInline):
    model = Students
    extra = 2

# 注册方式二---装饰器
# @admin.register(GradesAdmin)
#定义类来修改后台内容显示样式
class GradesAdmin(admin.ModelAdmin):
    # 关联对象
    inlines = [StudentsInfo]
    #列表属性
    list_display = ['pk','gname','gdate','ggirlnum','gboynum','isDelete'] #列表显示样式
    list_filter = ['gname'] #过滤字段
    search_fields = ['gname'] #定义后台搜索框
    list_per_page = 5 #分页

    #添加、修改页属性
    fields = ['ggirlnum','gboynum','gname','gdate','isDelete'] #规定属性的先后顺序
    # fieldsets = [
    #   ("num",{"fields":['ggirlnum','gboynum']}),
    #   ("base",{"fields":['gname','gdate','isDelete']}),
    # ] #给属性分组
    # 以上两个不可同时使用
    #
    # 执行动作相关
    actions_on_top = False
    actions_on_bottom = True
# 注册方式一
admin.site.register(Grades,GradesAdmin)

# class StudentsAdmin(admin.ModelAdmin):
#     list_display = ['pk','...']
    # 性别显示问题解决
#     def gender(self):
#       if self.sgender:
#           return "男"
#       else:
#           return "女"
#     gender.short_description = "性别"
#
#    其他中文显示同理可改
admin.site.register(Students)

class ArticlesAdmin(admin.ModelAdmin):
    #列表属性
    list_display = ['pk','aheadline','aauthor','aimage','atag'] #列表显示样式
    list_filter = ['aauthor','atag'] #过滤字段
    search_fields = ['aheadline','aauthor','atag'] #定义后台搜索框
    list_per_page = 10 #分页

    #添加、修改页属性
    fields = ['aheadline','aauthor','aimage','atag','adescription'] #规定属性的先后顺序
    # fieldsets = [
    #
    # ] #给属性分组
    # 以上两个不可同时使用
    #
    # 执行动作相关
    actions_on_top = False
    actions_on_bottom = True
admin.site.register(Articles,ArticlesAdmin)
