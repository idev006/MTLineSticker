from .frame_extractor import FrameExtractorModule
from .background_remover import BackgroundRemovalModule, BackgroundRemovalProvider, ClassicalBackgroundProvider
from .line_normalizer import LineNormalizerModule
from .submission import SubmissionModule

__all__ = [
    "FrameExtractorModule",
    "BackgroundRemovalModule",
    "BackgroundRemovalProvider",
    "ClassicalBackgroundProvider",
    "LineNormalizerModule",
    "SubmissionModule",
]
