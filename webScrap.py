from html.parser import HTMLParser


class LinkParser(HTMLParser):
    '''Analizador HTML que imprime el valor de el atributo
    href en las etiquetas de anclaje'''

    def handle_starttag(self, tag, attrs):
        'Imprime el valor del atributo href, si existe'
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    print(attr[1])