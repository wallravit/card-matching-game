# Setup argument
ARG PORT=5000
ARG PIP_REQUIREMENT_FILE=requirements.txt

FROM python:3.8.6-buster AS build
ARG PIP_REQUIREMENT_FILE
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-dev python-psycopg2 && \
    rm -rf /var/cache/apt/* /var/lib/apt/lists/* && \
    # timezone
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone
COPY dependencies /build/dependencies
WORKDIR /build
RUN pip3 wheel --wheel-dir=/wheels -r dependencies/$PIP_REQUIREMENT_FILE


FROM python:3.8.6-slim AS production
LABEL MAINTAINER "Wallravit Khamdee <wallravit@gmail.com.com>"

ARG PORT=5000
ARG PIP_REQUIREMENT_FILE=requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-dev python-psycopg2 && \
    rm -rf /var/cache/apt/* /var/lib/apt/lists/* && \
    # timezone
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone
RUN useradd -ms /bin/bash appuser

# Setup OS Environments
ENV APP_DIR=/home/appuser/app \
    PYTHONPATH=/home/appuser/app \
    APP_ENV=PRODUCTION \
    PORT=$PORT 

# Copy wheels from build container
COPY --from=build /wheels /wheels

USER appuser

# Add source code into application directory
COPY . $APP_DIR
# Change Working directory 
WORKDIR $APP_DIR
# Install python pip denpendencies via wheels

USER root

RUN pip3 install \
    --no-index \
    --find-links=/wheels \
    -r dependencies/$PIP_REQUIREMENT_FILE

USER appuser

ENTRYPOINT ["bash"]
CMD ["scripts/start_api.sh"]