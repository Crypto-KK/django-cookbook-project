from haystack import indexes


from demo_app.models import Idea


# 修改此处，类名为模型类的名称+Index，比如模型类为Articles,则这里类名为ArticlesIndex
class IdeaIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        # 修改此处，为你自己的model
        return Idea

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
