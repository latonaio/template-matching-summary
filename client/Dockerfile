FROM latonaio/l4t:latest

ENV POSITION=Runtime \
    SERVICE=template-matching-summary \
    AION_HOME="/var/lib/aion"

# Setup Directoties
RUN mkdir -p ${AION_HOME}/$POSITION/$SERVICE
WORKDIR ${AION_HOME}/$POSITION/$SERVICE/

ADD client .

CMD ["python3", "-u" ,"main.py"]
