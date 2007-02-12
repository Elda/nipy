"""
These classes provide the most basic structures required by
the Image class.
"""

__docformat__ = 'restructuredtext'

from neuroimaging.core.reference.grid import SamplingGrid
from neuroimaging.data_io import DataSource

class BaseImage(object):
    """
    This class defines a minimal interface which different types of images
    should implement. This interface is used by the `image.Image` class, which is
    the class which should be used by applications.
    """

    def __init__(self, data, grid, dtype):
        self.grid = grid
        self.data = data
        self.dtype = dtype
        
    def __getitem__(self, item):
        return self.data[item]
        
    def __setitem__(self, item, value):
        self.data[item] = value

    def asfile(self):
        """ Return image filename corresponding to `image.image.Image` object data.

        :Returns: ``string``
            
        :Raises NotImplemenetedError: Subclasses must implement this.       
        """
        raise NotImplementedError

class ArrayImage (BaseImage):
    """A simple class to mimic an image file from an array."""
    def __init__(self, data, grid=None):
        """
        Create an `ArrayImage` instance from an array,
        by default assumed to be 3d.

        Example
        -------
        
        >>> from numpy import zeros
        >>> from neuroimaging.core.image.base_image import ArrayImage
        >>> z = ArrayImage(zeros((10,20,20)))
        >>> print z.grid.ndim
        3
        
        """
        grid = grid and grid or SamplingGrid.identity(data.shape)
        dtype = data.dtype
        BaseImage.__init__(self, data, grid, dtype)

    def asfile(self):        
        """ Return image filename corresponding to `image.image.Image` object data.

        :Returns: ``string``
        """
        filename = DataSource().tempfile(".img", "nipy-")
        return filename
