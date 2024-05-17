from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from .models import library


# 手写序列化器
class order(serializers.Serializer):
    book_name = serializers.CharField(max_length=100)
    book_author = serializers.CharField(max_length=100)
    book_price = serializers.FloatField()

    def create(self, validated_data):
        return library.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(instance.id)  # 这url的值
        print(validated_data)  # 这是data传过来的值
        library.objects.filter(id=instance.id).update(**validated_data)
        new_data = library.objects.get(id=instance.pk)
        return new_data
    #     return  library.objects.filter(pk=instance.id).update(**validated_data)


class rers(APIView):
    # 获取所有书籍
    def get(self, req):
        rers1 = library.objects.all()
        self.order1 = order(instance=rers1, many=True)
        return Response(self.order1.data, status=200)

    # 添加书籍
    def post(self, req):
        self.inster = req.data
        order_version2 = order(data=self.inster, )  # 实现反序列化
        if order_version2.is_valid():  # 验证和实例化类
            order_version2.save()  # 实现插入
            # 返回包含修改后状态码的响应
            return Response(order_version2.data, status=200)
        else:
            return Response(order_version2.errors)


class single_operation(APIView):
    def get(self, req, id):
        substance = order(instance=library.objects.get(pk=2))
        return Response(substance.data)

    def put(self, req, id):
        # 获取请求数据
        substance = req.data
        # 获取要更新的库对象
        data1 = library.objects.get(pk=id)
        # 使用序列化器进行数据验证和更新
        serializer = order(instance=data1, data=substance)
        if serializer.is_valid():
            """ library.objects.filter(pk=id).update(**serializer.validated_data)
            new_data=library.objects.get(pk=id)
            serializer.instance=new_data
           #  这是不重写作业uqdate
           """
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, req, id):
        pass


# 序列化器继承
class automatic_order(serializers.ModelSerializer):
    # 作用进行了自动绑定和内部自己重写了save的方法
    class Meta:
        model = library
        fields = '__all__'  # 表示所有字段

        # exclue=['id'] 排除
        # 我们可以使用**extra_kwargs**参数为ModelSerializer添加或修改原有的选项参数
# 正常apiview可以使用实例化器
class automatic_sers(APIView):
    # 获取所有书籍
    def get(self, req):
        rers1 = library.objects.all()
        self.order1 = automatic_order(instance=rers1, many=True)
        return Response(self.order1.data, status=200)
    # 添加书籍
    def post(self, req):
        self.inster = req.data
        order_version2 = automatic_order(data=self.inster, )  # 实现反序列化
        if order_version2.is_valid():  # 验证和实例化类
            order_version2.save()  # 实现插入
            # 返回包含修改后状态码的响应
            return Response(order_version2.data, status=200)
        else:
            return Response(order_version2.errors)
# genericapiview
class sers_automaic_rank(serializers.ModelSerializer):
    class Meta:
        model = library
        fields = '__all__'
# genericapiview相当与帮你简化了里面的model.objects.all()把他提前出为类的共享变量直接可以通过self.get_queryset()来调用
#和简化序列器的调用直接在共享变量定义了serializer_class获取序列器以后类里面直接通过调用self.get_serializer
class sers_gener(GenericAPIView):
    queryset = library.objects.all()
    serializer_class = sers_automaic_rank

    def get(self, req):
        self._substance = self.get_serializer(instance=self.get_queryset(), many=True)
        return Response(self._substance.data, status=200)

    def post(self, req):
        automatic_substance = req.data
        self._substance_version2 = self.get_serializer(data=automatic_substance)
        if self._substance_version2.is_valid():
            self._substance_version2.save()
            return Response(self._substance_version2.data)
        else:
            return Response(self._substance_version2.errors)
# self.get_object() 相当与帮你执行了获取url的id然后执行了library.objects.all().filter(id=pk).first()获取了实例对象
class sers_gener_version2(GenericAPIView):
    queryset = library.objects.all()
    serializer_class = sers_automaic_rank
    def get(self,req,pk):
        self.substance=self.get_serializer(instance=self.get_object(),many=False)
        return Response(self.substance.data,status=200)
    def put(self,req,pk):
        self.substance_version2 = self.get_serializer(data=req.data,instance=self.get_object(),many=False)
        if self.substance_version2.is_valid():
            self.substance_version2.save()
            return Response(self.substance_version2.data)
        else:
            return Response(self.substance_version2.errors)
    def delete(self,req,pk):
        self.get_object().delete()
        return Response(status=204)

#混入参数可以简单的理解为直接帮我们封装了增删改查的逻辑要我们直接传入相应对象直接调用api完成功能但这直接影向了灵活性
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
class sers_gener_version3(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = library.objects.all()
    serializer_class = sers_automaic_rank
    def get(self,req):
        return self.list(req)
    def post(self,request):
        return self.create(request)

class sers_gener_version4(GenericAPIView,ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):
    queryset = library.objects.all()
    serializer_class = sers_automaic_rank
    def get(self,req,pk):
        return self.retrieve(req,pk)
    def put(self,req,pk):
        return self.update(req,pk)
    def delete(self,req,pk):
        return self.destroy(req,pk)

#进一步封装更加的方便
#对上面几个get等等增删改查的请求在次封装我们只要提供序列化器和数据
class sers_gener_version5(ListCreateAPIView):
    queryset = library.objects.all()
    serializer_class = sers_automaic_rank
class sers_gener_version6(RetrieveUpdateDestroyAPIView):
    queryset = library.objects.all()
    serializer_class = sers_automaic_rank
#在进一步简化
# 这里是对上面两个的进一步简化我们可以自定义get等等请求进入到那个函数而不是之前一样get请求一定要对应get函数我们可以在路由那里配置
class automaic_utensil(serializers.ModelSerializer):
    class  Meta:
        model = library
        fields = '__all__'
from rest_framework.viewsets import ViewSet
#简单测试用例
class automaic_utensil_viewset(ViewSet):
    def get_all(self,req):
        return Response("我是获取全部")
    def post_create(self,req):
        return Response("我是创建")
    def get_one(self,req,pk):
        return Response("我是获取一个")
    def put_update(self,req,pk):
        return Response("我是更新")
    def delete_delete(self,req,pk):
        return Response("我是删除")
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
class automaic_utensil_viewset2(GenericViewSet,ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = library.objects.all()
    serializer_class = automaic_utensil
from rest_framework.viewsets import ModelViewSet
#上面导入直接继承了GenericViewSet,ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
# 这里则是基础了上面几步操作直接封装直接在路由那里配置直接调用类类里面提供序列化器和数据即可这样极大的限制了灵活
class automaic_utensil_viewset3(ModelViewSet):
    queryset = library.objects.all()
    serializer_class = automaic_utensil


#测试案例
class test_day1(ModelViewSet):
    queryset = library.objects.all()
    serializer_class = automaic_utensil

