require 'anemone'

root = ARGV[0]

def get_host_without_www(url)
  url = "http://#{url}" if URI.parse(url).scheme.nil?
  host = URI.parse(url).host.downcase
  host = host.start_with?('www.') ? host[4..-1] : host
  host = host.start_with?('www2.') ? host[5..-1] : host
end

puts "url"
i = 0
Anemone.crawl(root, :discard_page_bodies => true, :depth_limit => 5) do |anemone|
  anemone.on_every_page do |page|
      puts page.url
  end
  
  anemone.focus_crawl do |page|
    if page.redirect_to and get_host_without_www(page.url.to_s) == get_host_without_www(page.redirect_to.to_s)
        [page.redirect_to]
    else
        page.links
    end
  end
end