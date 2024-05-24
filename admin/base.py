from sqladmin import ModelView


class BaseView(ModelView):
    form_include_pk = True
