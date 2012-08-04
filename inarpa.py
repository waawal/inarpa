# https://.github.com/waawal/inarpa/
# License: BSD

def create(ip, suffix='in-addr.arpa'):
    """ Reverses the ipv4 so that it can be checked with a dnsbl or the like,
        >>> create(ip='89.218.52.234', suffix='ix.dnsbl.manitu.net')
        '234.52.218.89.ix.dnsbl.manitu.net.'
    """
    reverse = '.'.join(reversed(ip.split('.')))
    return '{reverse}.{suffix}.'.format(reverse=reverse, suffix=suffix)
