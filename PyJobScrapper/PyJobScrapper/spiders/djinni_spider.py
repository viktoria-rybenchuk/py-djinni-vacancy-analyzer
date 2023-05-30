import csv

import scrapy

from .utills import TECHNOLOGIES


class DjinniSpider(scrapy.Spider):
    name = "djinni"
    start_urls = ["https://djinni.co/jobs/?all-keywords=&any-of-keywords=&exclude-keywords=&primary_keyword=Python"]
    results = []

    def parse(self, response, **kwargs):
        vacancies = response.css("li.list-jobs__item")

        for vacancy in vacancies:
            job_title = vacancy.css("a.profile span::text").get()
            company_name = vacancy.css("div.list-jobs__details__info a::text").get().strip()
            additional_info = vacancy.css("div.list-jobs__description div.text-card::text").getall()
            additional_info = [info.strip() for info in additional_info if info.strip()]

            details_info = vacancy.css("div.list-jobs__details__info")
            experience = details_info.css("nobr:contains('досвіду')::text").extract_first().split()[1]
            experience = 0 if not experience.isdigit() else int(experience)
            english_text = details_info.css(
                "nobr:contains('Intermediate')::text, nobr:contains('Advanced')::text").extract_first()
            english_level = english_text.split()[-1] if english_text is not None else None

            viewers_span = vacancy.css("div.text-date span[data-toggle='tooltip']::attr(title)").get()
            viewers_count = int(viewers_span.split()[0]) if viewers_span else None

            applicants_span = vacancy.css("div.text-date span[data-toggle='tooltip']::attr(title)").getall()[-1]
            applicants_count = int(applicants_span.split()[0]) if applicants_span else None

            mentioned_technologies = [tech for tech in TECHNOLOGIES if
                                      any(tech.lower() in info.lower() for info in additional_info)]
            data = {
                "Job Title": job_title,
                "Company Name": company_name,
                "English Level": english_level,
                "Experience": experience,
                "Technologies": mentioned_technologies,
                "Viewers": viewers_count,
                "Applicants": applicants_count
            }

            self.results.append(data)

        next_page = response.css(
            "ul.pagination.pagination_with_numbers li.page-item.active + li.page-item a.page-link::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def closed(self, reason):
        filename = "scraped_data.csv"
        with open(filename, "w", newline="") as csvfile:
            fieldnames = ["Job Title", "Company Name", "English Level", "Experience", "Technologies", "Viewers",
                          "Applicants"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(self.results)
