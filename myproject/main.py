import argparse

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


cli_parser = argparse.ArgumentParser()
cli_parser.add_argument('-f', '--filename', help='filename')


def main(filename):
    target_urls = [
        'https://www.ptt.cc/bbs/Gossiping/M.1559788476.A.074.html',
        'https://www.ptt.cc/bbs/Gossiping/M.1557928779.A.0C1.html'
    ]
    process = CrawlerProcess(get_project_settings())
    process.crawl('ptt_crawler', start_urls=target_urls, filename=filename)
    process.start()


if __name__ == '__main__':
    args = cli_parser.parse_args()
    main(args.filename)
