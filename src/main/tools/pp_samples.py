from jinja2 import Template

sample_1 = """{{ service_name }} privacy policy

This document describes how we collect, use and protect your personal information within the {{ service_name }} service.

Data collected

{% for data_type in data_types %} - {{ data_type }}
{% endfor %}
Data retention

Your personal data will be stored for the following period: {{ retention_period }}.

Usage

We use your personal data for the following purposes:
- Customize our services.
- Contacting you about matters relating to the service.
- We will contact you to help us with our services and to provide you with information about our services.

Rights
We may use your data to help us improve our services and to provide you with information to help us improve our service.We may use your data to help us improve our customer service and to help us improve our customer service:
{% for right in user_rights %} - {{ right }}
{% endfor %}
Changes
We reserve the right to make changes to this privacy policy. We will notify you of any changes."""

sample_2 = """Privacy Policy for {{ service_name }}

In this document, we outline how we collect, use, and protect your personal information within the {{ service_name }} service.

Collected Data
{% for data_type in data_types %} - {{ data_type }}
{% endfor %}
Data Retention
Your personal data will be stored for the following period: {{ retention_period }}.

Usage
We use your personal data for the following purposes:
- Customizing our services.
- Contacting you regarding service-related matters.
- Statistical analysis and improvement of user experience.

Rights
You have the following rights regarding your data:
{% for right in user_rights %} - {{ right }}
{% endfor %}
Modifications
We reserve the right to modify this privacy policy. You will be notified of any changes."""

sample_3 = """Privacy Policy for {{ service_name }}

In this document we explain how we collect, use and protect your personal data as part of the {{ service_name }} service.

Data collected
{% for data_type in data_types %} - {{ data_type }}
{% endfor %}
Retention of data
Your personal data will be stored for the following period: {{ retention_period }}.

Utilisation
We use your personal data for the following purposes:
- Customisation of our services.
- Contacting you in relation to service-related matters.
- Statistical analysis and improvement of user experience.

Your rights
You have the following rights in relation to your data:
{% for right in user_rights %} - {{ right }}
{% endfor %}
Changes
We reserve the right to change this Privacy Policy. You will be notified of any changes."""

sample_4 = """Privacy policy for {{ service_name }}

In this document, we explain how we collect, use and protect your personal data as part of the {{ service_name }} service.

Data collected
{% for data_type in data_types %} - {{ data_type }}
{% endfor %}
Retention of data
Your personal data will be retained for the following period: {{ retention_period }}.

Use
We use your personal data for the following purposes:
- Customisation of our services.
- Contacting you in connection with service-related matters.
- Statistical analysis and improvement of the user experience.

Your rights
You have the following rights in relation to your data:
{% for right in user_rights %} - {{ right }}
{% endfor %}
Changes
We reserve the right to change this Privacy Policy. You will be notified of any changes."""

sample_5 = """Privacy policy for {{ service_name }}

In this document, we explain how we collect, use and protect your personal data as part of the {{ service_name }} service.

Data collected
{% for data_type in data_types %} - {{ data_type }}
{% endfor %}
Retention of data
Your personal data will be retained for the following period: {{ retention_period }}.

Use
We use your personal data for the following purposes:
- Customisation of our services.
- Contacting you in connection with service-related matters.
- Statistical analysis and improvement of the user experience.

Your rights
You have the following rights in relation to your data:
{% for right in user_rights %} - {{ right }}
{% endfor %}
Changes
We reserve the right to change this Privacy Policy. You will be notified of any changes."""


sample_6 = """{{ service_name }} Terms and Conditions

These Terms and Conditions ("Terms", "Terms and Conditions") govern your use of the {{ service_name }} service operated by [Company Name] ("us", "we", or "our").

Please read these Terms and Conditions carefully before using our service.
Your access to and use of the service is conditioned on your acceptance of and compliance with these Terms. These Terms apply to all visitors, users, and others who access or use the service.
By accessing or using the service you agree to be bound by these Terms. If you disagree with any part of the terms, then you may not access the service.

Data Collection and Use
This section outlines how we collect, process, and protect your personal information within the {{ service_name }} service.

Data Types Collected
{% for data_type in data_types %} - {{ data_type }}
{% endfor %}
Data Retention
Your personal data will be stored for the following period: {{ retention_period }}.

Usage of Personal Data
We utilize your personal data for the following purposes:
- Customizing our services.
- Contacting you regarding service-related matters.
- Improving and enhancing our services.
- Providing information about our services.

User Rights
You have the following rights regarding your personal data:
{% for right in user_rights %} - {{ right }}
{% endfor %}
Changes to Terms and Conditions
We reserve the right to modify or replace these Terms and Conditions at any time. If a revision is material, we will try to provide at least 30 days' notice prior to any new terms taking effect. What constitutes a material change will be determined at our sole discretion.
By continuing to access or use our service after those revisions become effective, you agree to be bound by the revised terms. If you do not agree to the new terms, please stop using the service.

Contact Us
If you have any questions about these Terms and Conditions, please contact us."""


sample_7 = """{{ service_name }} Service Terms of Use

Welcome to {{ service_name }}. These terms of use govern your access to and use of the {{ service_name }} service.

Data Collection and Use
We collect and use your personal information within the {{ service_name }} service for the following data types:
{% for data_type in data_types %} - {{ data_type }}
{% endfor %}
Data Retention
Your personal data will be stored for a duration of {{ retention_period }}.

Usage
We use your personal data for:
- Customizing our services.
- Contacting you regarding the service.
- Improving our services.

User Rights
You have the following rights regarding your data:
{% for right in user_rights %} - {{ right }}
{% endfor %}
Changes
We reserve the right to modify these terms. We will notify you of any changes.
"""

sample_8 = """Terms of Service for {{ service_name }}

By using the {{ service_name }} service, you agree to these terms.

Data Collection
We collect the following data types:
{% for data_type in data_types %} - {{ data_type }}
{% endfor %}
Data Retention
Your personal data will be retained for {{ retention_period }}.

Usage
We use your data for:
- Customizing our services.
- Service-related communication.

User Rights
You have the right to:
{% for right in user_rights %} - {{ right }}
{% endfor %}
Changes
We reserve the right to update these terms. We will inform you of any modifications.
"""

sample_9 = """Terms of Service and Privacy Agreement

Thank you for using {{ service_name }}. These terms govern your use of our service.

1. Data Collection
We collect various data types:
{% for data_type in data_types %} - {{ data_type }}
{% endfor %}
2. Data Retention
Your data is stored for {{ retention_period }}.

3. Usage
We use your data for:
- Personalizing services.
- Contacting you about our service.

4. User Rights
You have rights to:
{% for right in user_rights %} - {{ right }}
{% endfor %}
5. Changes
We reserve the right to update these terms. We will notify you of any modifications.
"""

sample_10 = """{{ service_name }} Terms and Conditions

Your use of {{ service_name }} is subject to the following terms:

Data Collection:
{% for data_type in data_types %} - {{ data_type }}
{% endfor %}
Retention Period:
{{ retention_period }}

Usage:
We use your data for the following purposes:
- Personalization of services.
- Communication related to the service.

User Rights:
You have the following rights:
{% for right in user_rights %} - {{ right }}
{% endfor %}
Changes:
We may revise these terms. Updates will be communicated to you.
"""

sample_11 = """Terms of Use for {{ service_name }}

Data Handling:
We collect data types such as:
{% for data_type in data_types %} - {{ data_type }}
{% endfor %}
Data Retention:
Your information is stored for {{ retention_period }}.

Service Usage:
Your data is utilized for:
- Customizing services.
- Service-related correspondence.

User Rights:
You have the right to:
{% for right in user_rights %} - {{ right }}
{% endfor %}
Changes and Updates:
We reserve the right to modify these terms. Any changes will be communicated.
"""


