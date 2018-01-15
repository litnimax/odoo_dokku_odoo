FROM odoo

USER root

RUN apt-get update && apt-get install -y procps net-tools vim

WORKDIR /

ADD ./entrypoint.py /
ADD ./nginx.conf.sigil /
ADD ./Procfile /

# Copy Odoo addons
COPY ./addons/ /mnt/extra-addons/

EXPOSE 8069 8072

USER odoo
ENTRYPOINT ["/entrypoint.py"]
CMD ["odoo"]
