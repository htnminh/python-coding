with open('urls_out.txt', 'w') as opf:
    with open('urls.txt', 'r') as ipf:
        for url in ipf:
            opf.write('\item \\url{%s}\n' % url.strip())
            
    