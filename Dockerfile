FROM wernight/dante
ADD . /etc/
RUN chmod 755 /etc/sockd.conf \
    && printf '123qwe\n123qwe\n' | adduser denis
