from app.models import Category, Product


def load_categoreis():
    return Category.query.order_by('id').all()


def load_products(kw=None):
    query = Product.query

    return query.all()
