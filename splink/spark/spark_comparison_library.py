from ..comparison_library import (
    ArrayIntersectAtSizesComparisonBase,
    DamerauLevenshteinAtThresholdsComparisonBase,
    DateDiffAtThresholdsComparisonBase,
    DistanceFunctionAtThresholdsComparisonBase,
    DistanceInKMAtThresholdsComparisonBase,
    ExactMatchBase,
    JaccardAtThresholdsComparisonBase,
    JaroAtThresholdsComparisonBase,
    JaroWinklerAtThresholdsComparisonBase,
    LevenshteinAtThresholdsComparisonBase,
)
from .spark_base import (
    SparkBase,
)
from .spark_comparison_level_library import (
    array_intersect_level,
    damerau_levenshtein_level,
    datediff_level,
    distance_function_level,
    distance_in_km_level,
    else_level,
    exact_match_level,
    jaccard_level,
    jaro_level,
    jaro_winkler_level,
    levenshtein_level,
    null_level,
)


class SparkComparisonProperties(SparkBase):
    @property
    def _exact_match_level(self):
        return exact_match_level

    @property
    def _null_level(self):
        return null_level

    @property
    def _else_level(self):
        return else_level

    @property
    def _array_intersect_level(self):
        return array_intersect_level

    @property
    def _datediff_level(self):
        return datediff_level

    @property
    def _distance_in_km_level(self):
        return distance_in_km_level

    @property
    def _levenshtein_level(self):
        return levenshtein_level

    @property
    def _damerau_levenshtein_level(self):
        return damerau_levenshtein_level

    @property
    def _jaro_winkler_level(self):
        return jaro_winkler_level

    @property
    def _jaccard_level(self):
        return jaccard_level


class exact_match(SparkComparisonProperties, ExactMatchBase):
    pass


class distance_function_at_thresholds(
    SparkComparisonProperties, DistanceFunctionAtThresholdsComparisonBase
):
    @property
    def _distance_level(self):
        return distance_function_level


class levenshtein_at_thresholds(
    SparkComparisonProperties, LevenshteinAtThresholdsComparisonBase
):
    @property
    def _distance_level(self):
        return levenshtein_level

class damerau_levenshtein_at_thresholds(
    SparkComparisonProperties, DamerauLevenshteinAtThresholdsComparisonBase
):
    @property
    def _distance_level(self):
        return damerau_levenshtein_level


class jaro_at_thresholds(SparkComparisonProperties, JaroAtThresholdsComparisonBase):
    @property
    def _distance_level(self):
        return jaro_level


class jaro_winkler_at_thresholds(
    SparkComparisonProperties, JaroWinklerAtThresholdsComparisonBase
):
    @property
    def _distance_level(self):
        return jaro_winkler_level


class jaccard_at_thresholds(
    SparkComparisonProperties, JaccardAtThresholdsComparisonBase
):
    @property
    def _distance_level(self):
        return jaccard_level


class array_intersect_at_sizes(
    SparkComparisonProperties, ArrayIntersectAtSizesComparisonBase
):
    pass


class datediff_at_thresholds(
    SparkComparisonProperties, DateDiffAtThresholdsComparisonBase
):
    pass


class distance_in_km_at_thresholds(
    SparkComparisonProperties, DistanceInKMAtThresholdsComparisonBase
):
    pass
