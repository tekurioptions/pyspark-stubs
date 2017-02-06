# PySpark Stubs

A collection of the Apache Spark [stub files](https://www.python.org/dev/peps/pep-0484/#stub-files). These files were generated by [stubgen](https://github.com/python/mypy/blob/master/mypy/stubgen.py) and manually edited to include accurate type hints.

Tests and configuration files have been originally contributed to the [Typeshed project](https://github.com/python/typeshed/). Please refer to its [contributors list](https://github.com/python/typeshed/graphs/contributors) and [license](https://github.com/python/typeshed/blob/master/LICENSE) for details.


## Usage

According to [PEP 484](https://www.python.org/dev/peps/pep-0484/#storing-and-distributing-stub-files): 

> Third-party stub packages can use any location for stub storage. Type checkers should search for them using PYTHONPATH. 

Moreover:

> Third-party stub packages can use any location for stub storage. Type checkers should search for them using PYTHONPATH. A default fallback directory that is always checked is shared/typehints/python3.5/ (or 3.6, etc.)

Adding `third_party/3` to the `PYTHONPATH` seems to the trick.

## Version Compatibility

Currently this project uses Spark 2.1.0 as a reference.

## API Coverage

| Module                                             | Dynamically typed | Statically typed | Notes            |
|----------------------------------------------------|-------------------|------------------|------------------|
| pyspark                                            | ✔                 | ✘                |                  |
| pyspark.accumulators                               | ✔                 | ✘                |                  |
| pyspark.broadcast                                  | ✔                 | ✔                | Mixed            |
| <s>pyspark.cloudpickle</s>                         | ✘                 | ✘                | Internal         |
| pyspark.conf                                       | ✘                 | ✔                |                  |
| pyspark.context                                    | ✘                 | ✔                |                  |
| <s>pyspark.daemon</s>                              | ✘                 | ✘                | Internal         |
| pyspark.files                                      | ✘                 | ✔                |                  |
| <s>pyspark.find\_spark\_home</s>                   | ✘                 | ✘                | Internal         |
| <s>pyspark.heapq3</s>                              | ✘                 | ✘                | Internal         |
| <s>pyspark.java\_gateway</s>                       | ✘                 | ✘                | Internal         |
| pyspark.join                                       | ✔                 | ✘                |                  |
| pyspark.ml                                         | ✔                 | ✘                |                  |
| pyspark.ml.base                                    | ✔                 | ✘                |                  |
| pyspark.ml.classification                          | ✔                 | ✘                |                  |
| pyspark.ml.clustering                              | ✔                 | ✘                |                  |
| pyspark.ml.common                                  | ✔                 | ✘                |                  |
| pyspark.ml.evaluation                              | ✔                 | ✘                |                  |
| pyspark.ml.feature                                 | ✔                 | ✘                |                  |
| pyspark.ml.linalg                                  | ✔                 | ✘                |                  |
| pyspark.ml.param                                   | ✔                 | ✘                |                  |
| <s>pyspark.ml.param._shared_params\_code\_gen</s>  | ✘                 | ✘                | Internal         |
| pyspark.ml.param.shared                            | ✔                 | ✘                |                  |
| pyspark.ml.pipeline                                | ✔                 | ✘                |                  |
| pyspark.ml.recommendation                          | ✔                 | ✘                |                  |
| pyspark.ml.regression                              | ✔                 | ✘                |                  |
| pyspark.ml.tests                                   | ✘                 | ✘                |                  |
| pyspark.ml.tuning                                  | ✔                 | ✘                |                  |
| pyspark.ml.util                                    | ✔                 | ✘                |                  |
| pyspark.ml.wrapper                                 | ✔                 | ✘                |                  |
| pyspark.mllib                                      | ✔                 | ✘                |                  |
| pyspark.mllib.classification                       | ✔                 | ✘                |                  |
| pyspark.mllib.clustering                           | ✔                 | ✘                |                  |
| pyspark.mllib.common                               | ✔                 | ✘                |                  |
| pyspark.mllib.evaluation                           | ✔                 | ✘                |                  |
| pyspark.mllib.feature                              | ✔                 | ✘                |                  |
| pyspark.mllib.fpm                                  | ✔                 | ✘                |                  |
| pyspark.mllib.linalg                               | ✘                 | ✔                |                  |
| pyspark.mllib.linalg.distributed                   | ✔                 | ✘                |                  |
| pyspark.mllib.random                               | ✔                 | ✘                |                  |
| pyspark.mllib.recommendation                       | ✔                 | ✘                |                  |
| pyspark.mllib.regression                           | ✔                 | ✘                |                  |
| pyspark.mllib.stat                                 | ✔                 | ✘                |                  |
| pyspark.mllib.stat.KernelDensity                   | ✔                 | ✘                |                  |
| pyspark.mllib.stat._statistics                     | ✔                 | ✘                |                  |
| pyspark.mllib.stat.distribution                    | ✔                 | ✘                |                  |
| pyspark.mllib.stat.test                            | ✔                 | ✘                |                  |
| <s>pyspark.mllib.tests</s>                         | ✘                 | ✘                | Tests            |
| pyspark.mllib.tree                                 | ✔                 | ✘                |                  |
| pyspark.mllib.util                                 | ✔                 | ✘                |                  |
| pyspark.profiler                                   | ✔                 | ✘                |                  |
| pyspark.rdd                                        | ✘                 | ✔                |                  |
| pyspark.rddsampler                                 | ✔                 | ✘                |                  |
| pyspark.resultiterable                             | ✔                 | ✘                |                  |
| pyspark.serializers                                | ✔                 | ✘                |                  |
| <s>pyspark.shell</s>                               | ✘                 | ✘                | Internal         |
| <s>pyspark.shuffle</s>                             | ✘                 | ✘                | Internal         |
| pyspark.sql                                        | ✔                 | ✘                |                  |
| pyspark.sql.catalog                                | ✘                 | ✔                |                  |
| pyspark.sql.column                                 | ✘                 | ✔                |                  |
| pyspark.sql.conf                                   | ✘                 | ✔                |                  |
| pyspark.sql.context                                | ✘                 | ✔                |                  |
| pyspark.sql.dataframe                              | ✘                 | ✔                |                  |
| pyspark.sql.functions                              | ✘                 | ✔                |                  |
| pyspark.sql.group                                  | ✘                 | ✔                |                  |
| pyspark.sql.readwriter                             | ✘                 | ✔                |                  |
| pyspark.sql.session                                | ✘                 | ✔                |                  |
| pyspark.sql.streaming                              | ✔                 | ✘                |                  |
| <s>pyspark.sql.tests</s>                           | ✘                 | ✘                | Tests            |
| pyspark.sql.types                                  | ✔                 | ✘                |                  |
| pyspark.sql.utils                                  | ✔                 | ✘                |                  |
| pyspark.sql.window                                 | ✘                 | ✔                |                  |
| pyspark.statcounter                                | ✔                 | ✘                |                  |
| pyspark.status                                     | ✔                 | ✘                |                  |
| pyspark.storagelevel                               | ✘                 | ✔                |                  |
| pyspark.streaming                                  | ✔                 | ✘                |                  |
| pyspark.streaming.context                          | ✔                 | ✘                |                  |
| pyspark.streaming.dstream                          | ✔                 | ✘                |                  |
| pyspark.streaming.flume                            | ✔                 | ✘                |                  |
| pyspark.streaming.kafka                            | ✔                 | ✘                |                  |
| pyspark.streaming.kinesis                          | ✔                 | ✘                |                  |
| pyspark.streaming.listener                         | ✔                 | ✘                |                  |
| <s>pyspark.streaming.tests</s>                     | ✘                 | ✘                | Tests            |
| pyspark.streaming.util                             | ✔                 | ✘                |                  |
| <s>pyspark.tests</s>                               | ✘                 | ✘                | Tests            |
| <s>pyspark.traceback\_utils</s>                    | ✘                 | ✘                | Internal         |
| pyspark.version                                    | ✘                 | ✔                |                  |
| <s>pyspark.worker</s>                              | ✘                 | ✘                | Internal         |

## Disclaimer

Apache Spark, Spark, Apache, and the Spark logo are <a href="https://www.apache.org/foundation/marks/">trademarks</a> of
  <a href="http://www.apache.org">The Apache Software Foundation</a>. This project is not owned, endorsed, or sponsored by The Apache Software Foundation.
