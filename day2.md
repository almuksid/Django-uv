# Django Template Language Cheatsheet

> A comprehensive quick reference for Django's template syntax

---

## Table of Contents
1. [Variables](#variables)
2. [Filters](#filters)
3. [Tags](#tags)
4. [Comments](#comments)
5. [Template Inheritance](#template-inheritance)
6. [Built-in Filters Reference](#built-in-filters-reference)
7. [Built-in Tags Reference](#built-in-tags-reference)
8. [CSRF & Security](#csrf--security)
9. [Static Files](#static-files)
10. [Custom Filters & Tags](#custom-filters--tags)

---

## Variables

### Displaying Variables
```django
{{ variable_name }}
{{ user.username }}
{{ article.title }}
```

### Variable Default Values
```django
{{ variable|default:"Nothing" }}
{{ variable|default_if_none:"None" }}
```

---

## Filters

### Basic Filter Syntax
```django
{{ variable|filter_name }}
{{ variable|filter_name:"argument" }}
{{ name|lower }}
{{ price|floatformat:2 }}
```

### Chaining Filters
```django
{{ text|escape|linebreaks }}
{{ name|truncatewords:10|lower }}
```

### Filter with Safe Content
```django
{{ html_content|safe }}  # Disable auto-escaping
```

---

## Tags

### Control Flow Tags

#### `{% if %}` - Conditional Rendering
```django
{% if user.is_authenticated %}
    Welcome, {{ user.username }}!
{% elif user.is_new %}
    Please complete your profile
{% else %}
    Please log in
{% endif %}
```

#### `{% if %}` Operators
```django
{% if age >= 18 %}
    Adult
{% endif %}

{% if "admin" in user.groups %}
    Admin access
{% endif %}

{% if user.is_authenticated and user.is_staff %}
    Staff user
{% endif %}

{% if not user.is_banned %}
    Active user
{% endif %}
```

#### `{% for %}` - Loops
```django
{% for item in items %}
    {{ item.name }}
{% empty %}
    No items found
{% endfor %}
```

#### `{% for %}` Loop Variables
```django
{% for user in users %}
    {{ forloop.counter }}         # Current iteration (1-indexed)
    {{ forloop.counter0 }}        # Current iteration (0-indexed)
    {{ forloop.revcounter }}      # Reverse counter
    {{ forloop.revcounter0 }}     # Reverse counter (0-indexed)
    {{ forloop.first }}           # First iteration?
    {{ forloop.last }}            # Last iteration?
    {{ forloop.parentloop }}      # Parent loop context
{% endfor %}
```

---

## Comments

### Single-line Comments (Not Rendered)
```django
{# This is a comment #}
{# multi-line
    comment #}
```

### Multi-line Comment Template
```django
{% comment %}
    This is a multi-line comment
    Anything here will be removed
{% endcomment %}
```

---

## Template Inheritance

### Base Template (`base.html`)
```django
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
    {% block extra_css %}{% endblock %}
</head>
<body>
    {% block header %}{% endblock %}

    <main>
        {% block content %}{% endblock %}
    </main>

    {% block footer %}{% endblock %}
    {% block extra_js %}{% endblock %}
</body>
</html>
```

### Child Template
```django
{% extends "base.html" %}

{% block title %}{{ page.title }} - My Site{% endblock %}

{% block content %}
    <h1>{{ page.heading }}</h1>
    {{ page.body|safe }}
{% endblock %}

{% block extra_css %}
    {{ block.super }}
    <link rel="stylesheet" href="/static/page.css">
{% endblock %}
```

### Block Super (Inherit Parent Content)
```django
{% block content %}
    {{ block.super }}  # Include parent block content
    <p>Additional content</p>
{% endblock %}
```

---

## Built-in Filters Reference

### String Filters

| Filter | Description | Example |
|--------|-------------|---------|
| `lower` | Converts to lowercase | `{{ name\|lower }}` |
| `upper` | Converts to uppercase | `{{ name\|upper }}` |
| `title` | Title case | `{{ text\|title }}` |
| `capitalize` | First char uppercase | `{{ text\|capitalize }}` |
| `truncatechars:n` | Truncate to n chars | `{{ text\|truncatechars:20 }}` |
| `truncatewords:n` | Truncate to n words | `{{ text\|truncatewords:5 }}` |
| `wordcount` | Count words | `{{ text\|wordcount }}` |
| `length` | Return length | `{{ list\|length }}` |
| `length_is:n` | Length equals n? | `{{ list\|length_is:3 }}` |
| `ljust:n` | Left-align in n chars | `{{ text\|ljust:10 }}` |
| `rjust:n` | Right-align in n chars | `{{ text\|rjust:10 }}` |
| `center:n` | Center in n chars | `{{ text\|center:10 }}` |
| `cut:pattern` | Remove pattern | `{{ text\|cut:" " }}` |
| `join:str` | Join with string | `{{ list\|join:", " }}` |

### Number Filters

| Filter | Description | Example |
|--------|-------------|---------|
| `add:n` | Add n | `{{ num\|add:5 }}` |
| `sub:n` | Subtract n | `{{ num\|sub:3 }}` |
| `floatformat:n` | Round to n decimals | `{{ price\|floatformat:2 }}` |
| `filesizeformat` | Human-readable size | `{{ bytes\|filesizeformat }}` |

### List Filters

| Filter | Description | Example |
|--------|-------------|---------|
| `first` | First item | `{{ list\|first }}` |
| `last` | Last item | `{{ list\|last }}` |
| `slice:n:m` | Slice list | `{{ list\|slice:":2" }}` |
| `random` | Random item | `{{ list\|random }}` |
| `dictsort:key` | Sort by key | `{{ dict\|dictsort:"age" }}` |
| `dictsortreversed:key` | Sort descending | `{{ dict\|dictsortreversed:"age" }}` |
| `unordered_list` | Nested UL/LI | `{{ list\|unordered_list }}` |

### Date/Time Filters

| Filter | Description | Example |
|--------|-------------|---------|
| `date:format` | Format date | `{{ date\|date:"D d M Y" }}` |
| `time:format` | Format time | `{{ time\|time:"H:i" }}` |
| `timesince:val` | Time since | `{{ date\|timesince:now }}` |
| `timeuntil:val` | Time until | `{{ date\|timeuntil:now }}` |

### HTML/Text Filters

| Filter | Description | Example |
|--------|-------------|---------|
| `escape` | HTML escape | `{{ html\|escape }}` |
| `safe` | Mark as safe | `{{ html\|safe }}` |
| `linebreaks` | Convert newlines to `<p>` | `{{ text\|linebreaks }}` |
| `linebreaksbr` | Convert newlines to `<br>` | `{{ text\|linebreaksbr }}` |
| `urlize` | Convert URLs to links | `{{ text\|urlize }}` |
| `urlizetrunc:n` | Truncate URL links | `{{ text\|urlizetrunc:15 }}` |
| `striptags` | Strip HTML tags | `{{ html\|striptags }}` |
| `removetags` | Remove specific tags | `{{ html\|removetags:"script style" }}` |

### Boolean & Logic Filters

| Filter | Description | Example |
|--------|-------------|---------|
| `default:value` | Default if falsy | `{{ var\|default:"N/A" }}` |
| `default_if_none:value` | Default if None | `{{ var\|default_if_none:"N/A" }}` |
| `yesno:"a,b,c"` | Yes/No/Maybe mapping | `{{ flag\|yesno:"Yes,No,Maybe" }}` |
| `divisibleby:n` | Divisible by n? | `{{ num\|divisibleby:3 }}` |

### Other Useful Filters

| Filter | Description | Example |
|--------|-------------|---------|
| `slugify` | Convert to slug | `{{ title\|slugify }}` |
| `escapejs` | Escape for JavaScript | `{{ text\|escapejs }}` |
| `json_script` | JSON in script tag | `{{ data\|json_script:"data-id" }}` |
| `localize` | Localize output | `{{ value\|localize }}` |
| `localtime` | Convert to local time | `{{ date\|localtime }}` |
| `urlencode` | URL encode | `{{ text\|urlencode }}` |

---

## Built-in Tags Reference

### Definition & Assignment

| Tag | Description | Example |
|-----|-------------|---------|
| `block` | Define block | `{% block content %}` |
| `extends` | Extend template | `{% extends "base.html" %}` |
| `include` | Include template | `{% include "snippet.html" %}` |
| `load` | Load template library | `{% load static %}` |

### Control Flow

| Tag | Description | Example |
|-----|-------------|---------|
| `if` | Conditional | `{% if condition %}` |
| `elif` | Else if | `{% elif condition %}` |
| `else` | Else | `{% else %}` |
| `endif` | End if | `{% endif %}` |
| `for` | Loop | `{% for item in items %}` |
| `empty` | Empty loop case | `{% empty %}` |
| `endfor` | End for | `{% endfor %}` |
| `ifequal` | If equal (deprecated) | `{% ifequal a b %}` |
| `ifnotequal` | If not equal (deprecated) | `{% ifnotequal a b %}` |

### Iteration Helpers

| Tag | Description | Example |
|-----|-------------|---------|
| `cycle` | Cycle through values | `{% cycle 'odd' 'even' %}` |
| `resetcycle` | Reset cycle | `{% resetcycle %}` |
| `firstof` | First non-empty variable | `{% firstof var1 var2 "fallback" %}` |

### Template Organization

| Tag | Description | Example |
|-----|-------------|---------|
| `autoescape` | Auto-escaping block | `{% autoescape off %}` |
| `filter` | Filter section | `{% filter lower %}` |
| `spaceless` | Remove whitespace | `{% spaceless %}` |
| `verbatim` | Disable template parsing | `{% verbatim %}` |

### Loops & Conditions

| Tag | Description | Example |
|-----|-------------|---------|
| `for ... empty` | Loop with empty case | `{% for i in items %}...{% empty %}None{% endfor %}` |
| `cycle` | Cycle through values | `{% cycle 'row1' 'row2' %}` |
| `widthratio` | Calculate ratio | `{% widthratio this_value max_value max_width %}` |
| `with` | Cache variable | `{% with total=business.employees.count %}` |

### HTML & Forms

| Tag | Description | Example |
|-----|-------------|---------|
| `csrf_token` | CSRF token | `{% csrf_token %}` |
| `url` | URL routing | `{% url 'view-name' param %}` |
| `static` | Static file URL | `{% static 'css/style.css' %}` |

### Debugging & Comments

| Tag | Description | Example |
|-----|-------------|---------|
| `comment` | Comment block | `{% comment %}...{% endcomment %}` |
| `debug` | Debug info | `{% debug %}` |

### Internationalization

| Tag | Description | Example |
|-----|-------------|---------|
| `trans` | Translation | `{% trans "Text" %}` |
| `blocktrans` | Block translation | `{% blocktrans %}...{% endblocktrans %}` |
| `language` | Switch language | `{% language 'en' %}` |
| `get_available_languages` | Available langs | `{% get_available_languages as langs %}` |
| `get_current_language` | Current language | `{% get_current_language as lang %}` |

### Time Zones

| Tag | Description | Example |
|-----|-------------|---------|
| `timezone` | Set timezone | `{% timezone "UTC" %}` |
| `get_current_timezone` | Get timezone | `{% get_current_timezone as tz %}` |
| `localtime` | Enable local time | `{% localtime on %}` |

### Other Tags

| Tag | Description | Example |
|-----|-------------|---------|
| `now` | Current date/time | `{% now "jS F Y H:i" %}` |
| `regroup` | Regroup list | `{% regroup people by gender as gender_list %}` |
| `lorem` | Lorem ipsum text | `{% lorem 3 p random %}` |

---

## CSRF & Security

### CSRF Token in Forms
```django
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```

### CSRF Token in AJAX
```django
<script>
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
</script>
```

### Safe Content (Disable Auto-escaping)
```django
{{ html_content|safe }}
{% autoescape off %}
    {{ html_content }}
{% endautoescape %}
```

---

## Static Files

### Loading Static Files
```django
{% load static %}
```

### Static File URL
```django
<link rel="stylesheet" href="{% static 'css/style.css' %}">
<script src="{% static 'js/app.js' %}"></script>
<img src="{% static 'images/logo.png' %}" alt="Logo">
```

### Static Files in CSS
```django
{% load static %}
{% static "css/style.css" as style_css %}
<link rel="stylesheet" href="{{ style_css }}">
```

---

## Custom Filters & Tags

### Directory Structure
```
myapp/
├── templatetags/
│   ├── __init__.py
│   └── myapp_tags.py
```

### Custom Filter
```python
# templatetags/myapp_tags.py
from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg

@register.filter(name='custom_upper')
def custom_upper_filter(value):
    return value.upper()
```

### Usage in Template
```django
{% load myapp_tags %}
{{ price|multiply:2 }}
{{ name|custom_upper }}
```

### Custom Simple Tag
```python
@register.simple_tag
def current_time(format_string):
    return datetime.now().strftime(format_string)

@register.simple_tag(takes_context=True)
def current_user(context):
    return context['request'].user
```

### Usage in Template
```django
{% load myapp_tags %}
{% current_time "%Y-%m-%d %H:%M" %}
{% current_user %}
```

### Custom Inclusion Tag
```python
@register.inclusion_tag('myapp/snippet.html')
def show_results(results):
    return {'results': results}
```

### Usage in Template
```django
{% load myapp_tags %}
{% show_results poll.results %}
```

---

## Template Context Processors

### Built-in Context Processors
```django
# settings.py
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
}]
```

### Accessing in Templates
```django
{{ request.path }}
{{ request.user.username }}
{{ request.META.HTTP_USER_AGENT }}
{{ messages }}
```

---

## Quick Examples

### Pagination
```django
{% for object in page_obj %}
    {{ object.name }}
{% endfor %}

<div class="pagination">
    <span class="page-links">
        {% if page_obj.has_previous %}
            <a href="?page=1">&laquo; first</a>
            <a href="?page={{ page_obj.previous_page_number }}">previous</a>
        {% endif %}
        <span class="page-current">
            Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}
        </span>
        {% if page_obj.has_next %}
            <a href="?page={{ page_obj.next_page_number }}">next</a>
            <a href="?page={{ page_obj.paginator.num_pages }}">last &raquo;</a>
        {% endif %}
    </span>
</div>
```

### Form Rendering
```django
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}        {# Paragraph rendering #}
    {{ form.as_table }}    {# Table rendering #}
    {{ form.as_ul }}       {# List rendering #}

    {# Manual rendering #}
    {{ form.non_field_errors }}
    {% for field in form %}
        <div class="field">
            {{ field.label_tag }}
            {{ field }}
            {{ field.errors }}
            {% if field.help_text %}
                <small>{{ field.help_text }}</small>
            {% endif %}
        </div>
    {% endfor %}
    <button type="submit">Submit</button>
</form>
```

### Messages
```django
{% if messages %}
    <div class="messages">
        {% for message in messages %}
            <div class="message {{ message.tags }}">
                {{ message }}
            </div>
        {% endfor %}
    </div>
{% endif %}
```

---

## Date Formatting Codes

| Code | Description | Example Output |
|------|-------------|----------------|
| `a` | 'a.m.' or 'p.m.' | 'p.m.' |
| `A` | 'AM' or 'PM' | 'PM' |
| `b` | Month, textual, 3 letters | 'Jan' |
| `d` | Day of month, 2 digits | '01' to '31' |
| `D` | Day of week, 3 letters | 'Fri' |
| `E` | Month, locale specific | 'listopada' |
| `f` | Time, 12-hour | '1', '1:30' |
| `F` | Month, textual, long | 'January' |
| `g` | Hour, 12-hour | '1' to '12' |
| `G` | Hour, 24-hour | '0' to '23' |
| `h` | Hour, 12-hour, 2 digits | '01' to '12' |
| `H` | Hour, 24-hour, 2 digits | '00' to '23' |
| `i` | Minutes | '00' to '59' |
| `I` | Daylight Savings | '1', '0' |
| `j` | Day of month | '1' to '31' |
| `l` | Day of week, full | 'Friday' |
| `L` | Leap year? | 'True', 'False' |
| `m` | Month, 2 digits | '01' to '12' |
| `M` | Month, 3 letters | 'Jan' |
| `n` | Month | '1' to '12' |
| `N` | Month abbreviation | 'Jan' |
| `O` | Difference to GMT | '+0200' |
| `P` | Time | '1 a.m.', '1:30 p.m.' |
| `r` | RFC 2822 | 'Thu, 21 Dec 2000 16:01:07' |
| `s` | Seconds, 2 digits | '00' to '59' |
| `S` | English ordinal suffix | 'st', 'nd', 'rd', 'th' |
| `t` | Days in month | '28' to '31' |
| `T` | Time zone | 'EST', 'MDT' |
| `u` | Microseconds | '0' to '999999' |
| `w` | Day of week | '0' (Sunday) to '6' (Saturday) |
| `W` | ISO-8601 week | '1', '53' |
| `y` | Year, 2 digits | '99' |
| `Y` | Year, 4 digits | '1999' |
| `z` | Day of year | '0' to '365' |
| `Z` | Time zone offset | '-43200' to '43200' |

---

## Tips & Best Practices

1. **Use `{% load %}`** at the top of your template after `{% extends %}`
2. **Always use `{% csrf_token %}`** in POST forms
3. **Use `{% block super %}`** to extend parent block content
4. **Cache expensive operations** with `{% with %}` tag
5. **Use `{% static %}`** instead of hardcoded paths
6. **Avoid complex logic** in templates - keep it in views
7. **Use `{% spaceless %}`** to remove extra whitespace
8. **Custom filters** should return values, not print output
9. **Template inheritance** reduces code duplication significantly
10. **Use `{% include %}`** for reusable components

---

## Resources

- [Official Django Template Docs](https://docs.djangoproject.com/en/stable/topics/templates/)
- [Built-in Tags Reference](https://docs.djangoproject.com/en/stable/ref/templates/builtins/)
- [Built-in Filters Reference](https://docs.djangoproject.com/en/stable/ref/templates/builtins/#std-templatetags-ref)

---

*Generated for Django Template Language Quick Reference*
