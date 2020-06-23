=============
API reference
=============

Top-level functions
===================

.. automodule:: proplot.ui

.. autosummary:: proplot.ui
   :toctree: api

   proplot.ui.SubplotsContainer
   proplot.ui.close
   proplot.ui.show
   proplot.ui.subplots


Figure class
============

.. automodule:: proplot.figure

.. autosummary:: proplot.figure
   :toctree: api

   proplot.figure.Figure


Axes classes
============

.. automodule:: proplot.axes

.. autosummary:: proplot.axes
   :toctree: api

   proplot.axes.Axes
   proplot.axes.BasemapAxes
   proplot.axes.CartesianAxes
   proplot.axes.CartopyAxes
   proplot.axes.GeoAxes
   proplot.axes.PolarAxes
   proplot.axes.bar_wrapper
   proplot.axes.barh_wrapper
   proplot.axes.boxplot_wrapper
   proplot.axes.cmap_changer
   proplot.axes.colorbar_wrapper
   proplot.axes.cycle_changer
   proplot.axes.default_latlon
   proplot.axes.default_transform
   proplot.axes.fill_between_wrapper
   proplot.axes.fill_betweenx_wrapper
   proplot.axes.hlines_wrapper
   proplot.axes.indicate_error
   proplot.axes.legend_wrapper
   proplot.axes.scatter_wrapper
   proplot.axes.standardize_1d
   proplot.axes.standardize_2d
   proplot.axes.text_wrapper
   proplot.axes.violinplot_wrapper
   proplot.axes.vlines_wrapper


Constructor functions
=====================

.. automodule:: proplot.constructor

.. autosummary:: proplot.constructor
   :toctree: api

   proplot.constructor.Colormap
   proplot.constructor.Colors
   proplot.constructor.Cycle
   proplot.constructor.Formatter
   proplot.constructor.Locator
   proplot.constructor.Norm
   proplot.constructor.Proj
   proplot.constructor.Scale

Configuration tools
===================

.. automodule:: proplot.config

.. autosummary:: proplot.config
   :toctree: api

   proplot.config.RcConfigurator
   proplot.config.config_inline_backend
   proplot.config.rc
   proplot.config.register_cmaps
   proplot.config.register_colors
   proplot.config.register_cycles
   proplot.config.register_fonts
   proplot.config.use_style


Plotting wrappers
=================

.. automodule:: proplot.axes.plot

.. autosummary:: proplot.axes
   :toctree: api


Demo functions
==============

.. automodule:: proplot.demos

.. autosummary:: proplot.demos
   :toctree: api

   proplot.demos.show_channels
   proplot.demos.show_cmaps
   proplot.demos.show_colors
   proplot.demos.show_colorspaces
   proplot.demos.show_cycles
   proplot.demos.show_fonts


Colormaps and normalizers
=========================

.. automodule:: proplot.colors

.. autosummary:: proplot.colors
   :toctree: api

   proplot.colors.ColorDatabase
   proplot.colors.ColormapDatabase
   proplot.colors.DiscreteNorm
   proplot.colors.DivergingNorm
   proplot.colors.LinearSegmentedColormap
   proplot.colors.LinearSegmentedNorm
   proplot.colors.ListedColormap
   proplot.colors.PerceptuallyUniformColormap
   proplot.colors.make_mapping_array

Locators and formatters
=======================

.. automodule:: proplot.ticker

.. autosummary:: proplot.ticker
   :toctree: api

   proplot.ticker.AutoFormatter
   proplot.ticker.FracFormatter
   proplot.ticker.LatitudeLocator
   proplot.ticker.LongitudeLocator
   proplot.ticker.SciFormatter
   proplot.ticker.SigFigFormatter
   proplot.ticker.SimpleFormatter


Axis scale classes
==================

.. automodule:: proplot.scale

.. autosummary:: proplot.scale
   :toctree: api

   proplot.scale.CutoffScale
   proplot.scale.ExpScale
   proplot.scale.FuncScale
   proplot.scale.InverseScale
   proplot.scale.LinearScale
   proplot.scale.LogScale
   proplot.scale.LogitScale
   proplot.scale.MercatorLatitudeScale
   proplot.scale.PowerScale
   proplot.scale.SineLatitudeScale
   proplot.scale.SymmetricalLogScale


Cartopy projections
===================

.. automodule:: proplot.crs

.. autosummary:: proplot.crs
   :toctree: api

   proplot.crs.Aitoff
   proplot.crs.Hammer
   proplot.crs.KavrayskiyVII
   proplot.crs.NorthPolarAzimuthalEquidistant
   proplot.crs.NorthPolarGnomonic
   proplot.crs.NorthPolarLambertAzimuthalEqualArea
   proplot.crs.SouthPolarAzimuthalEquidistant
   proplot.crs.SouthPolarGnomonic
   proplot.crs.SouthPolarLambertAzimuthalEqualArea
   proplot.crs.WinkelTripel


Gridspec classes
================

.. automodule:: proplot.gridspec

.. autosummary:: proplot.gridspec
   :toctree: api

   proplot.gridspec.GridSpec
   proplot.gridspec.SubplotSpec


Miscellaneous tools
===================

.. automodule:: proplot.utils

.. autosummary:: proplot.utils
   :toctree: api

   proplot.utils.arange
   proplot.utils.edges
   proplot.utils.edges2d
   proplot.utils.scale_luminance
   proplot.utils.scale_saturation
   proplot.utils.set_alpha
   proplot.utils.set_hue
   proplot.utils.set_luminance
   proplot.utils.set_saturation
   proplot.utils.to_rgb
   proplot.utils.to_rgba
   proplot.utils.to_xyz
   proplot.utils.to_xyza
   proplot.utils.units
