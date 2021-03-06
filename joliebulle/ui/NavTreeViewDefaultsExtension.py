from plugins.ExtensionPoints import NavTreeViewExtensionPoint
from PyQt4 import QtCore
from ui.RecipeView import RecipeView

__author__ = 'nico'

class NavTreeViewDefaultsExtension(NavTreeViewExtensionPoint):
    def __init__(self):
        self.model = [
            {'id':'recipes',
             'label':QtCore.QCoreApplication.translate(__name__, '''Recettes'''),
             'items' : [
                {
                 'id':'recipes.all',
                 'label':QtCore.QCoreApplication.translate(__name__, '''Toutes''')
               }
               ]
            },
            {'id':'catalog',
             'label':QtCore.QCoreApplication.translate(__name__, '''Catalogue'''),
             'items' : []
            },
            {'id':'tools',
             'label':QtCore.QCoreApplication.translate(__name__, '''Outils'''),
             'items' : []
            }
        ]
        self.recipe_view = RecipeView()

    def get_items(self, parentId=None):
        if parentId is None :
            #return list of parent items from model
            rootItems = []
            for item in self.model:
                rootItems.append({'id':item['id'], 'label':item['label']})
            return rootItems
        else:
            #return list of subitems
            children = []
            for item in self.model:
                if item['id']==parentId:
                    children.extend(item['items'])
            return children

    def get_view(self, window, item):
        if 'recipes' == item.id:
            return self.recipe_view
        return None
