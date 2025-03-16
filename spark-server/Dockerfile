FROM bitnami/spark:3.5.5
USER root
RUN install_packages curl
USER 1001
# Install custom jars
# https://github.com/bitnami/containers/tree/main/bitnami/spark#installing-additional-jars
RUN curl https://repo1.maven.org/maven2/org/apache/spark/spark-connect_2.12/3.5.5/spark-connect_2.12-3.5.5.jar --output /opt/bitnami/spark/jars/spark-connect_2.12-3.5.5.jar && \
    curl https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-spark-runtime-3.5_2.12/1.8.1/iceberg-spark-runtime-3.5_2.12-1.8.1.jar --output /opt/bitnami/spark/jars/iceberg-spark-runtime-3.5_2.12-1.8.1.jar
