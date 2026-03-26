from . import Esoteric, Proper

esoteric = Esoteric
proper = Proper

from .Esoteric.adhd import adhd_sort
from .Esoteric.bogo import bogo_sort
from .Esoteric.bozo import bozo_sort
from .Esoteric.intelligentdesign import intelligent_design_sort
from .Esoteric.miracle import miracle_sort
from .Esoteric.schrodinger import schrodinger_sort
from .Esoteric.sixseven import six_seven_sort
from .Esoteric.sleep import sleep_sort
from .Esoteric.stalin import stalin_sort
from .Esoteric.stooge import stooge_sort
from .Esoteric.thanos import thanos_sort
from .Proper.bubble import bubble_sort
from .Proper.count import counting_sort
from .Proper.heap import heap_sort
from .Proper.insertion import insertion_sort
from .Proper.merge import merge_sort
from .Proper.quick import quick_sort
from .Proper.radix import radix_sort
from .Proper.selection import selection_sort

__all__ = [
	"Proper",
	"Esoteric",
	"proper",
	"esoteric",
	"adhd_sort",
	"bogo_sort",
	"bozo_sort",
	"intelligent_design_sort",
	"miracle_sort",
	"schrodinger_sort",
	"six_seven_sort",
	"sleep_sort",
	"stalin_sort",
	"stooge_sort",
	"thanos_sort",
	"bubble_sort",
	"counting_sort",
	"heap_sort",
	"insertion_sort",
	"merge_sort",
	"quick_sort",
	"radix_sort",
	"selection_sort",
]

