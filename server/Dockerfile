FROM latonaio/l4t:latest

ENV POSITION=Runtime \
    SERVICE=template-matching-summary-server \
    AION_HOME="/var/lib/aion"

# Setup Directoties
RUN mkdir -p ${AION_HOME}/$POSITION/$SERVICE
WORKDIR ${AION_HOME}/$POSITION/$SERVICE/

ADD server .

CMD ["python3", "-u" ,"main.py"]
