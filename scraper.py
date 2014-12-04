import codecs
import json
import justext
import requests
import sys

s = requests.Session()

def get_content(url):
    content = ""
    try:
        r = s.get(url)
        if r.status_code == 200: #and r.headers['content-type'] == 'text/html':
            paragraphs = justext.justext(r.text, justext.get_stoplist("Spanish"))
            for paragraph in paragraphs:
              if not paragraph.is_boilerplate:
                content += " " + paragraph.text
    except Exception as e:
        print(e.message)
    print(content)
    return content

def main(input_file, output_file):
    input_url_file = codecs.open(input_file, 'r', 'utf-8')
    contents = list()
    for url in input_url_file:
        url = url.strip()
        print("doing %s" % url)
        content = get_content(url)
        if content:
            item = {'url': url, 'content': content}
            contents.append(item)

    dumped_json = json.dumps(contents)
    output_file = codecs.open(output_file, 'w', 'utf-8')
    output_file.write(dumped_json)
    output_file.close()


if __name__ == "__main__":
    path_to_url_file = sys.argv[1]
    path_to_output_file = sys.argv[2]
    print("reading %s .. outputing to %s" %(path_to_url_file, path_to_output_file) )
    main(path_to_url_file, path_to_output_file)
