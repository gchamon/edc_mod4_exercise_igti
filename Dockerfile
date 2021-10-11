FROM apache/airflow:2.1.4-python3.9

USER root
RUN mkdir -p /opt/pycharm/skeletons/cache \
  && chmod -R 777 /opt/pycharm

USER airflow

