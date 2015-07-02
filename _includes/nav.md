{:.nav}
 - [![AIMS]({{ site.absoluteurl }}/logo.png "AIMS Program Home")]({{site.aimsghurl}})
 - [Workshop Home]({% include url.lq %}/)
{% for topic in site.topics %} - {% if page.url contains topic.url %}{:.{{ site.css.active }}}{% endif %}{% include topic_link.md which=forloop.index0 %}
{% endfor %}
