FROM ubuntu:20.04
RUN apt-get update && \
    apt-get install -y cron

COPY docker/crontab_jobs /opt
RUN crontab /opt/crontab_jobs

# Create script activate environment
RUN echo 'source /opt/conda/bin/activate base && exec "$@"' > activate.sh
RUN chmod +x /activate.sh

ENTRYPOINT ["bash", "/activate.sh"]
CMD ["cron", "-f"]