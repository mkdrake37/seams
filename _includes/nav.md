{:.nav}
 - [![AIMS]({{ site.absoluteurl }}/logo.png "AIMS Program Home")]({{site.aimsghurl}})
 - [Workshop Home]({{ site.absoluteurl }}{{ site.baseurl }}/)
{% for topic in site.topics %} - {% if page.url contains topic.url %}{:.{{ site.css.active }}}{% endif %}{% include topic_link.md which=forloop.index0 %}
{% endfor %} - [Students]({{ site.absoluteurl }}{{ site.baseurl }}/students)<input type="button" value="RANDOM DRAW" onclick="pickStudent(this.nextSibling);"/><select style="display:none">{% assign current_students = site.students | where: "status", "current" %}{% for student in current_students %}
<option>{{ student.name }}</option>{% endfor %}
</select>
