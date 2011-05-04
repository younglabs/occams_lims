import zope.schema
from plone.directives import form
from hive.lab import MessageFactory as _
import zope.interface
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.app.dexterity.behaviors.related import IRelatedItems
from hive.lab.interfaces.specimen import ISpecimenBlueprint
from hive.lab.vocabularies import SpecimenVocabulary

class IContainsSpecimen(zope.interface.Interface):
    """
    Marker interface for items that contain Specimen Blueprints
    """
    pass
    
    
class ILab(form.Schema, IContainsSpecimen):
    """
    An Interface for the Labs
    """
    pass
    
class IClinicalLab(ILab):
    """
    An Interface for the Labs
    """
    pass
    
class IResearchLab(ILab):
    """
    An Interface for the Labs
    """
    pass
    
class ILabel(zope.interface.Interface):
    """
    Class that supports transforming an object into a label.
    """        
    patient_title = zope.schema.TextLine(
        title=u"Patient OUR#",
        readonly=True
        )
 
    study_title = zope.schema.TextLine(
        title=u"Study",
        readonly=True
        )
 
    protocol_title = zope.schema.TextLine(
        title=u"Protocol Week",
        readonly=True
        ) 
 
    date_collected = zope.schema.Date(
        title=u"Date",
        readonly=True
        ) 
        
class ILabelSheet(form.Schema):
    """
        info for building a pdf of labels
    """
    page_height = zope.schema.Float(
        title=_(u"Page Height"),
        required=True
        )
        
    page_width = zope.schema.Float(
        title=_(u"Page Width"),
        required=True
        )

    top_margin = zope.schema.Float(
        title=_(u"Top Margin"),
        required=True
        )
    side_margin = zope.schema.Float(
        title=_(u"Side Margin"),
        required=True
        )
    vert_pitch = zope.schema.Float(
        title=_(u"Vertical Pitch"),
        required=True
        )
        
    horz_pitch = zope.schema.Float(
        title=_(u"Horizontal Pitch"),
        required=True
        )
    label_height = zope.schema.Float(
        title=_(u"Label Height"),
        required=True
        )
    label_width = zope.schema.Float(
        title=_(u"Label Width"),
        required=True
        )
        
    label_round = zope.schema.Float(
        title=_(u"Label Round"),
        required=True
        )

    no_across = zope.schema.Int(
        title=_(u"Number Across"),
        required=True
        )

    no_down = zope.schema.Int(
        title=_(u"Number Down"),
        required=True
        )