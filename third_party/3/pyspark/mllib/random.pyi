# Stubs for pyspark.mllib.random (Python 3.5)
#

from typing import Any, Optional
from pyspark.context import SparkContext
from pyspark.rdd import RDD
from pyspark.mllib.linalg import Vector

class RandomRDDs:
    @staticmethod
    def uniformRDD(
        sc: SparkContext,
        size: int,
        numPartitions: Optional[int] = ...,
        seed: Optional[int] = ...,
    ) -> RDD[float]: ...
    @staticmethod
    def normalRDD(
        sc: SparkContext,
        size: int,
        numPartitions: Optional[int] = ...,
        seed: Optional[int] = ...,
    ) -> RDD[float]: ...
    @staticmethod
    def logNormalRDD(
        sc: SparkContext,
        mean: float,
        std: float,
        size: int,
        numPartitions: Optional[int] = ...,
        seed: Optional[int] = ...,
    ) -> RDD[float]: ...
    @staticmethod
    def poissonRDD(
        sc: SparkContext,
        mean: float,
        size: int,
        numPartitions: Optional[int] = ...,
        seed: Optional[int] = ...,
    ) -> RDD[float]: ...
    @staticmethod
    def exponentialRDD(
        sc: SparkContext,
        mean: float,
        size: int,
        numPartitions: Optional[int] = ...,
        seed: Optional[int] = ...,
    ) -> RDD[float]: ...
    @staticmethod
    def gammaRDD(
        sc: SparkContext,
        shape: float,
        scale: float,
        size: int,
        numPartitions: Optional[int] = ...,
        seed: Optional[int] = ...,
    ) -> RDD[float]: ...
    @staticmethod
    def uniformVectorRDD(
        sc: SparkContext,
        numRows: int,
        numCols: int,
        numPartitions: Optional[int] = ...,
        seed: Optional[int] = ...,
    ) -> RDD[Vector]: ...
    @staticmethod
    def normalVectorRDD(
        sc: SparkContext,
        numRows: int,
        numCols: int,
        numPartitions: Optional[int] = ...,
        seed: Optional[int] = ...,
    ) -> RDD[Vector]: ...
    @staticmethod
    def logNormalVectorRDD(
        sc: SparkContext,
        mean: float,
        std,
        numRows: int,
        numCols: int,
        numPartitions: Optional[int] = ...,
        seed: Optional[int] = ...,
    ) -> RDD[Vector]: ...
    @staticmethod
    def poissonVectorRDD(
        sc: SparkContext,
        mean: float,
        numRows: int,
        numCols: int,
        numPartitions: Optional[int] = ...,
        seed: Optional[int] = ...,
    ) -> RDD[Vector]: ...
    @staticmethod
    def exponentialVectorRDD(
        sc: SparkContext,
        mean: float,
        numRows: int,
        numCols: int,
        numPartitions: Optional[int] = ...,
        seed: Optional[int] = ...,
    ) -> RDD[Vector]: ...
    @staticmethod
    def gammaVectorRDD(
        sc: SparkContext,
        shape: float,
        scale: float,
        numRows: int,
        numCols: int,
        numPartitions: Optional[int] = ...,
        seed: Optional[int] = ...,
    ) -> RDD[Vector]: ...
