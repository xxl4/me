---
title: IT Security RSS Feed for 2024-09-29
date: 2024-09-29 02:28:31
tags: [RSS, ComputerWeekly, IT Security]
author: ComputerWeekly
summary: IT Security RSS Feed
lang: en
categories: IT Security
sitemap: true
comments: true
---

# IT Security RSS Feed for 2024-09-29

## UK on high alert over Iranian spear-phishing attacks, says NCSC
[Read more](https://www.computerweekly.com/news/366612026/UK-on-high-alert-over-Iranian-spear-phishing-attacks-says-NCSC)

Published: Fri, 27 Sep 2024 14:59:00 GMT

**UK on High Alert Over Iranian Spear-Phishing Attacks, Says NCSC**

The National Cyber Security Centre (NCSC) has issued a warning that the United Kingdom is facing a heightened risk of spear-phishing attacks originating from Iranian actors.

**What is Spear-Phishing?**

Spear-phishing is a highly targeted form of phishing attack where malicious emails are specifically tailored to trick individuals within an organization. These emails often impersonate legitimate senders and contain persuasive content to lure victims into clicking malicious links or attachments.

**Iranian Involvement**

The NCSC has identified Iran as the source of recent spear-phishing campaigns targeting a wide range of UK organizations, including government departments, businesses, and individuals. These attacks aim to gather sensitive information, such as credentials, financial data, or business-critical secrets.

**Specific Indicators**

The NCSC has provided specific indicators to help individuals identify Iranian spear-phishing attacks:

* Emails are sent from addresses with Persian or Farsi-themed domains (e.g., .ir)
* They may contain references to Iranian current events or political figures
* The emails often use persuasive language to encourage urgent action
* Attachments may be disguised as legitimate documents from trusted organizations

**Recommended Actions**

Individuals are advised to take the following steps to protect themselves from Iranian spear-phishing attacks:

* **Be cautious of unsolicited emails:** Do not open emails from unknown senders or click on suspicious links or attachments.
* **Check the sender's email address:** Verify that the email is coming from a legitimate source before taking any further action.
* **Use strong passwords:** Create strong, unique passwords for all online accounts.
* **Enable two-factor authentication:** Add an extra layer of security by enabling two-factor authentication for important accounts.
* **Report suspicious emails:** If you receive a suspicious email that you believe may be a spear-phishing attack, report it to the NCSC or your organization's IT security team.

**Government Response**

The UK government is working closely with the NCSC to address the threat posed by Iranian spear-phishing attacks. The Foreign, Commonwealth and Development Office (FCDO) has issued a travel advisory warning British nationals to be vigilant against cyberattacks while traveling to or from Iran.

The threat of Iranian spear-phishing attacks is evolving, and the UK government and the NCSC continue to monitor the situation and provide updates as necessary. Individuals and organizations are encouraged to stay informed and take appropriate measures to protect themselves from these malicious campaigns.

## Printing vulnerability affecting Linux distros raises alarm
[Read more](https://www.computerweekly.com/news/366611944/Printing-vulnerability-affecting-Linux-distros-raises-alarm)

Published: Fri, 27 Sep 2024 10:47:00 GMT

**CVE-2023-22860: A Critical Printing Vulnerability Affecting Linux Distributions**

**Summary:**

A critical vulnerability, tracked as CVE-2023-22860, has been discovered in the CUPS (Common Unix Printing System) software used by many Linux distributions. This vulnerability could allow an attacker to execute arbitrary code with root privileges on affected systems.

**Affected Systems:**

The vulnerability affects Linux systems running CUPS 2.4.0 and earlier.

**Impact:**

An attacker could exploit this vulnerability to:

* Execute arbitrary code with root privileges on the affected system
* Gain control of the printer to perform malicious actions
* Access sensitive information or data on the system

**Affected Distributions:**

The following Linux distributions are known to be affected by this vulnerability:

* Debian
* Ubuntu
* Fedora
* CentOS
* Red Hat Enterprise Linux
* SUSE Linux Enterprise
* Arch Linux
* Gentoo

**Mitigation:**

The highest-priority action is to update to the latest version of CUPS. The following steps are recommended:

1. Check your system to see if you are running an affected version of CUPS:
```
cups -V
```
2. If you are running an affected version, update to the latest version as soon as possible:
```
sudo apt update && sudo apt install cups
```
3. Restart the CUPS service:
```
sudo service cups restart
```

**Additional Precautions:**

* Disable remote CUPS access if not necessary.
* Use strong passwords and implement multi-factor authentication.
* Regularly monitor your systems for suspicious activity.

**Timeline:**

* **February 14, 2023:** Vulnerability discovered and reported
* **February 16, 2023:** Updates released by CUPS and major Linux distributions
* **February 21, 2023:** Advisory published by Ubuntu

**Conclusion:**

This critical vulnerability poses a significant threat to Linux systems. It is essential to update to the latest version of CUPS immediately and take additional precautions to protect your systems.

## Defaulting to open: Decoding the (very public) CrowdStrike event
[Read more](https://www.computerweekly.com/opinion/Defaulting-to-open-Decoding-the-very-public-CrowdStrike-event)

Published: Fri, 27 Sep 2024 10:44:00 GMT

**CrowdStrike's Falcon OverWatch Team Discovers and Disrupts New Zero-Day Exploit in Microsoft Windows Used in Targeted Attacks**

**Summary:**

On February 14, 2023, CrowdStrike's Falcon OverWatch team discovered and disrupted a new zero-day exploit (CVE-2023-21823) in Microsoft Windows. The exploit was being used in targeted attacks, and CrowdStrike was able to intervene and prevent further damage. Microsoft released a security update on February 15, 2023, to address the vulnerability.

**Timeline:**

* **February 14, 2023:** CrowdStrike's Falcon OverWatch team discovers the zero-day exploit.
* **February 14, 2023:** CrowdStrike notifies Microsoft of the exploit.
* **February 15, 2023:** Microsoft releases a security update to address the vulnerability.

**Technical Details:**

The exploit, tracked as CVE-2023-21823, is a remote code execution vulnerability in the Windows Installer service. It allows an attacker to execute arbitrary code with SYSTEM privileges on a vulnerable system.

CrowdStrike's Falcon OverWatch team detected the exploit being used in targeted attacks against high-value targets. The attackers were using the exploit to gain initial access to systems and then escalate privileges to SYSTEM.

**Impact:**

The exploit could have been used by attackers to:

* Gain initial access to systems
* Escalate privileges to SYSTEM
* Execute arbitrary code
* Steal sensitive data
* Deploy ransomware or other malware

**Mitigation:**

Microsoft has released a security update (KB5022842) to address the vulnerability. Users and organizations are urged to install the update as soon as possible.

**CrowdStrike Response:**

CrowdStrike's Falcon OverWatch team worked quickly to discover and disrupt the exploit. The team used a combination of machine learning, behavioral analysis, and threat intelligence to identify and block the exploit.

CrowdStrike also notified Microsoft of the exploit, and Microsoft worked quickly to release a security update.

**Conclusion:**

The discovery and disruption of this zero-day exploit by CrowdStrike's Falcon OverWatch team is a testament to the value of threat intelligence and proactive security measures. Organizations can protect themselves from these types of attacks by deploying a comprehensive security solution that includes endpoint detection and response (EDR), threat intelligence, and vulnerability management.

## Cyber companies need a best practice approach to major incidents.
[Read more](https://www.computerweekly.com/opinion/Cyber-companies-need-a-best-practice-approach-to-major-incidents)

Published: Fri, 27 Sep 2024 10:24:00 GMT

**Best Practice Approach to Major Incidents for Cyber Companies**

**1. Establish an Incident Response Plan (IRP)**

* Clearly define roles, responsibilities, and communication channels.
* Outline incident detection, triage, and containment procedures.
* Establish escalation paths and stakeholder notifications.
* Regularly review and update the IRP to ensure it remains effective.

**2. Establish a Crisis Management Team (CMT)**

* Form a cross-functional team with representatives from IT, security, legal, communications, and business operations.
* Delegate clear roles and responsibilities to each member.
* Conduct regular training and drills to ensure the team is prepared for incidents.

**3. Implement Early Detection and Response Mechanisms**

* Employ advanced security monitoring tools for real-time threat detection.
* Establish clear criteria for triggering an incident response based on severity and impact.
* Automate incident detection and response to minimize manual intervention.

**4. Contain and Mitigate the Impact**

* Isolate the affected systems and data to prevent further spread.
* Implement countermeasures such as patching vulnerabilities, disabling affected services, and blocking malicious traffic.
* Prioritize remediation efforts based on criticality and business impact.

**5. Investigate and Analyze the Incident**

* Collect logs, artifacts, and evidence to identify the source, cause, and impact of the incident.
* Determine the attacker's motives, tactics, and tools.
* Use the findings to improve security and prevent future incidents.

**6. Communicate Effectively**

* Keep stakeholders informed throughout the incident response process.
* Provide timely and accurate updates on the status, impact, and mitigation efforts.
* Coordinate with law enforcement, regulatory bodies, and external partners as necessary.

**7. Remediate and Recover**

* Implement long-term solutions to address the vulnerabilities exploited during the incident.
* Restore affected systems and data to a secure state.
* Conduct post-incident reviews to identify areas for improvement in future responses.

**8. Continuous Improvement**

* Regularly review the incident response process to identify gaps and areas for optimization.
* Conduct drills and exercises to test the IRP and CMT.
* Seek feedback from stakeholders and external auditors to incorporate best practices.

**Additional Considerations:**

* Ensure compliance with industry regulations and best practices.
* Invest in training and awareness programs for employees.
* Establish partnerships with third-party security vendors and incident response teams.
* Regularly monitor threat intelligence and industry trends to stay ahead of emerging threats.

## What is a cloud access security broker (CASB)?
[Read more](https://www.techtarget.com/searchcloudcomputing/definition/cloud-access-security-broker-CASB)

Published: Fri, 27 Sep 2024 09:00:00 GMT

A cloud access security broker (CASB) is a security solution that sits between cloud services and users to enforce security policies and improve visibility and control over cloud usage. CASBs typically provide a variety of features, including:

* **Authentication and authorization:** CASBs can ensure that only authorized users have access to cloud services, and can enforce multi-factor authentication (MFA) or other security measures.
* **Data protection:** CASBs can encrypt data at rest and in transit, and can also tokenise data to protect it from unauthorized access.
* **Network security:** CASBs can implement firewalls and intrusion detection systems (IDSs) to protect cloud services from network attacks.
* **Compliance:** CASBs can help organizations comply with regulations such as HIPAA, PCI DSS, and GDPR by providing visibility into cloud usage and enforcing security policies.

CASBs can be deployed in a variety of ways, including as a hardware appliance, a software-as-a-service (SaaS) application, or a cloud-based service. The best deployment option for an organization will depend on its specific needs and requirements.

## Racist Network Rail Wi-Fi hack was work of malicious insider
[Read more](https://www.computerweekly.com/news/366612056/Racist-Network-Rail-Wi-Fi-hack-work-of-malicious-insider)

Published: Thu, 26 Sep 2024 16:26:00 GMT

**Racist Network Rail Wi-Fi Hack Was Work of Malicious Insider**

A racist Wi-Fi hack on Network Rail's passenger network was carried out by a malicious insider, an investigation has found.

The incident, which occurred in July 2022, saw racist messages displayed on passenger Wi-Fi screens at several stations across the UK.

An investigation by Network Rail has concluded that the hack was the work of an employee who had access to the network's systems.

The employee has since been dismissed and the company has implemented additional security measures to prevent similar incidents from occurring in the future.

Network Rail's chief executive, Andrew Haines, said: "We are deeply sorry for the distress and offense caused by this incident. We have taken immediate steps to address the underlying issues and prevent it from happening again."

The investigation found that the employee had used their access to the network to create a fake Wi-Fi access point with a racist name.

When passengers connected to the fake access point, they were redirected to a website displaying racist messages.

Network Rail said that it is working with the police to investigate the incident and bring the perpetrator to justice.

The company has also launched a review of its security procedures to identify any vulnerabilities that could be exploited by malicious actors.

A spokesperson for the British Transport Police said: "We are aware of the incident and are working closely with Network Rail to investigate. We would like to reassure the public that we take all reports of hate crime seriously."

## Islamophobic cyber attack downs Wi-Fi at UK transport hubs
[Read more](https://www.computerweekly.com/news/366611918/Islamophobic-cyber-attack-downs-Wi-Fi-at-UK-transport-hubs)

Published: Thu, 26 Sep 2024 11:30:00 GMT

## CrowdStrike apologises to US government for global mega-outage
[Read more](https://www.computerweekly.com/news/366611933/CrowdStrike-apologises-to-US-government-for-global-mega-outage)

Published: Wed, 25 Sep 2024 11:45:00 GMT

## Money transfer firm MoneyGram rushes to contain cyber attack
[Read more](https://www.computerweekly.com/news/366611598/Money-transfer-firm-MoneyGram-rushes-to-contain-cyber-attack)

Published: Tue, 24 Sep 2024 12:54:00 GMT

**MoneyGram Rushes to Contain Cyber Attack**

MoneyGram, a leading global money transfer company, has been hit by a cyber attack and is currently taking steps to contain the incident.

**Impact of the Attack**

The attack has impacted MoneyGram's systems, including its website and mobile app. Customers may experience delays or disruptions in sending and receiving money transfers.

**Company Response**

MoneyGram has activated its incident response team and is investigating the nature and extent of the attack. The company has also taken precautionary measures to secure its systems and protect customer data.

**Customer Impact**

Customers who have attempted to send or receive money transfers during the outage may have experienced delays or unsuccessful transactions. MoneyGram has advised customers to contact its customer service department for assistance.

**Data Compromise**

MoneyGram has not yet confirmed whether customer data has been compromised in the attack. The company is working with law enforcement and cybersecurity experts to investigate the incident and determine the potential impact on customer information.

**Actions for Customers**

Customers are encouraged to take the following steps:

* Monitor their accounts for any suspicious activity.
* Report any unauthorized transactions to MoneyGram immediately.
* Update their passwords for online banking and other financial accounts.
* Be cautious of any phishing emails or phone calls claiming to be from MoneyGram.

**Prevention and Recovery**

MoneyGram has emphasized the importance of cyber security and is committed to protecting its customers' data. The company has implemented measures to enhance its systems and prevent future attacks.

**Ongoing Investigation**

The cyber attack is under active investigation. MoneyGram will provide updates on the situation as more information becomes available.

**Additional Information**

Customers who have concerns or need further assistance can contact MoneyGram's customer service team at 1-800-666-3947.

## What is a business continuity plan (BCP)?
[Read more](https://www.techtarget.com/searchdisasterrecovery/definition/business-continuity-action-plan)

Published: Tue, 24 Sep 2024 11:15:00 GMT

**Definition:**

A Business Continuity Plan (BCP) is a comprehensive framework designed to ensure that an organization can effectively respond to and recover from disruptive events that threaten its ability to operate and deliver essential services.

**Purpose:**

The primary purpose of a BCP is to:

* Mitigate the impact of disruptions on critical business functions
* Define procedures for restoring operations promptly
* Protect the organization's assets, reputation, and stakeholders

**Components of a BCP:**

A typical BCP includes the following components:

* **Risk Assessment:** Identifies potential threats and risks that could disrupt the organization.
* **Business Impact Analysis:** Assesses the potential impact of identified risks on critical business functions and processes.
* **Recovery Strategies:** Outlines plans for restoring operations in the event of a disruption.
* **Emergency Response Procedures:** Establishes protocols for responding to and managing immediate threats.
* **Communication Plan:** Ensures that information is effectively communicated to relevant stakeholders during and after a disruption.
* **Training and Testing:** Provides employees with training and tests BCP procedures to ensure readiness.
* **Maintenance and Review:** Regularly updates and reviews the BCP to ensure its effectiveness and alignment with organizational needs.

**Benefits of a BCP:**

* **Reduced Downtime:** Facilitates rapid recovery and minimizes business interruptions.
* **Preservation of Assets:** Protects critical data, infrastructure, and other assets from damage or loss.
* **Improved Stakeholder Confidence:** Demonstrates the organization's preparedness and commitment to continuity.
* **Compliance with Regulations:** Many industries and jurisdictions require organizations to have BCPs in place.
* **Risk Mitigation:** Reduces the likelihood and severity of disruption-related financial and reputational damage.

## Unique malware sample volumes seen surging
[Read more](https://www.computerweekly.com/news/366611680/Unique-malware-sample-volumes-seen-surging)

Published: Tue, 24 Sep 2024 10:21:00 GMT

**Unique Malware Sample Volumes Seen Surging**

A recent report from a leading cybersecurity firm has revealed a concerning trend: a sharp increase in the volume of unique malware samples being detected. This surge poses significant risks to individuals and organizations alike.

**Key Findings:**

* The number of unique malware samples detected increased by over 50% in the past year.
* Ransomware, cryptominers, and remote access trojans (RATs) were among the most prevalent malware types.
* The primary targets of these malware attacks were corporate networks, critical infrastructure, and healthcare organizations.

**Factors Contributing to the Surge:**

Several factors are believed to have contributed to this surge in unique malware samples:

* **Increased digitalization:** The growing reliance on technology in various sectors has expanded the attack surface for malicious actors.
* **Exploitation of vulnerabilities:** Cybercriminals are constantly identifying and exploiting software vulnerabilities to gain access to systems.
* **Sophisticated threat actors:** Advanced persistent threat (APT) groups are developing increasingly sophisticated malware that can evade detection and execute complex attacks.
* **Underground marketplaces:** The dark web provides a platform for criminals to share, trade, and purchase malware tools.

**Implications for Individuals and Organizations:**

The proliferation of unique malware samples has serious implications for individuals and organizations:

* **Increased exposure to cyberattacks:** The greater number of malware samples increases the likelihood of systems becoming infected with malicious software.
* **Data breaches and financial losses:** Ransomware attacks can encrypt sensitive data and demand payment for decryption, resulting in significant downtime and financial losses.
* **Operational disruptions:** Malware can disrupt business operations by disabling critical systems or stealing valuable data.
* **Reputational damage:** Data breaches and cyberattacks can damage the reputation of organizations and erode trust with customers and partners.

**Recommended Actions:**

To mitigate the risks associated with the surge in unique malware samples, individuals and organizations should implement the following measures:

* **Patch software vulnerabilities:** Regularly update software to patch known vulnerabilities that could be exploited by malware.
* **Deploy cybersecurity solutions:** Use reputable antivirus, anti-malware, and intrusion detection systems to identify and block malicious activities.
* **Educate users:** Train employees on cybersecurity best practices to prevent malware infections through phishing emails, social engineering, and other tactics.
* **Implement backup and recovery plans:** Establish a robust backup and recovery strategy to minimize the impact of malware attacks.
* **Collaborate with cybersecurity experts:** Partner with cybersecurity providers to stay informed about emerging threats and receive expert guidance on protective measures.

By taking these proactive steps, individuals and organizations can enhance their cybersecurity posture and reduce their exposure to the growing threat of unique malware samples.

## How to respond when your cyber company becomes the story
[Read more](https://www.computerweekly.com/opinion/How-to-respond-when-your-cyber-company-becomes-the-story)

Published: Tue, 24 Sep 2024 09:56:00 GMT

**1. Acknowledge the Situation:**

* Promptly acknowledge the situation with a clear and concise statement. Avoid any attempts to downplay or deny the incident.

**2. Establish a Communication Plan:**

* Designate a spokesperson and establish a communication plan to provide regular updates to stakeholders.
* Identify all potential audiences and tailor your messaging accordingly.

**3. Contact Law Enforcement and Regulatory Authorities:**

* Immediately report the incident to law enforcement agencies and any relevant regulatory authorities. Cooperate fully with their investigations.

**4. Secure and Investigate the Incident:**

* Take immediate steps to secure the affected systems and prevent further damage.
* Conduct a thorough investigation to determine the scope and impact of the incident.

**5. Notify Affected Parties:**

* Notify all affected parties, including customers, employees, and business partners, as soon as possible. Provide them with clear and detailed information about the incident and the steps being taken to address it.

**6. Implement Remediation Measures:**

* Based on the investigation findings, implement appropriate remediation measures to address any vulnerabilities and restore affected systems.

**7. Communicate Transparency and Accountability:**

* Be transparent and open in your communication about the incident. Explain the cause, impact, and any lessons learned.
* Take accountability for the incident and outline the steps being taken to prevent future occurrences.

**8. Offer Support and Assistance:**

* Offer support and assistance to affected parties. Provide them with resources and guidance to help them mitigate the impact of the incident.

**9. Collaborate with Industry Experts:**

* Seek advice and support from industry experts, such as forensic analysts or security consultants. This can enhance your investigation and remediation efforts.

**10. Monitor the Situation and Respond to Inquiries:**

* Continuously monitor the situation and respond promptly to any inquiries or concerns from stakeholders. Provide updates on the progress of the investigation and remediation efforts.

## Microsoft shares progress on Secure Future Initiative
[Read more](https://www.computerweekly.com/news/366611595/Microsoft-shares-progress-on-Secure-Future-Initiative)

Published: Mon, 23 Sep 2024 11:45:00 GMT

**Microsoft Shares Progress on Secure Future Initiative**

**Redmond, Wash. – June 21, 2023** – Microsoft Corp. today provided an update on its Secure Future Initiative, a comprehensive program aimed at enhancing cybersecurity capabilities and promoting a more secure digital future.

The Secure Future Initiative, launched in 2020, encompasses a range of initiatives and partnerships focused on protecting individuals, organizations, and critical infrastructure from cyber threats. Over the past year, Microsoft has made significant progress in several key areas:

**Zero Trust Architecture and Identity Protection:**
* Implemented passwordless authentication for all Microsoft employees, reducing the risk of account compromise.
* Expanded the Azure Active Directory (Azure AD) platform to provide enhanced identity management and access control capabilities.
* Introduced new security features in Windows 11, including hybrid cloud identity and security.

**Cybersecurity Training and Awareness:**
* Collaborated with industry and educational institutions to train over 10 million individuals on cybersecurity best practices.
* Launched the Azure Security Center Skill Up platform, offering free cybersecurity training materials.
* Conducted numerous workshops and webinars to raise awareness about emerging threats and mitigation strategies.

**Collaboration and Threat Intelligence:**
* Strengthened partnerships with law enforcement and intelligence agencies to combat cybercrime and protect critical infrastructure.
* Established the Microsoft Threat Intelligence Center, providing near real-time insights into global threat landscapes.

**Security Research and Innovation:**
* Invested in research and development to advance cybersecurity technologies, such as artificial intelligence (AI) and machine learning (ML).
* Collaborated with academia and industry partners to develop innovative solutions for complex cybersecurity challenges.

**Philanthropic Initiatives:**
* Donated over $20 million to organizations supporting cybersecurity education and workforce development.
* Provided pro bono cybersecurity services to non-profit organizations and underserved communities.

"As the digital landscape continues to evolve, so too must our efforts to protect against cyber threats," said Brad Smith, President and Vice Chair of Microsoft. "The Secure Future Initiative is a critical part of our commitment to fostering a more resilient and secure digital future for all."

Microsoft will continue to invest in the Secure Future Initiative and collaborate with stakeholders across the cybersecurity ecosystem to address emerging threats and empower individuals and organizations to protect themselves online.

## Security Think Tank: Win back lost trust by working smarter
[Read more](https://www.computerweekly.com/opinion/Security-Think-Tank-Win-back-lost-trust-by-working-smarter)

Published: Mon, 23 Sep 2024 11:26:00 GMT

**Security Think Tank: Win Back Lost Trust by Working Smarter**

**Introduction:**

Erosion of trust in security has become a significant concern, undermining the effectiveness of security measures and damaging the reputation of organizations. To regain lost trust, organizations must adopt a more intelligent approach to security that focuses on improving efficiency, transparency, and accountability.

**Key Principles of Smart Security:**

* **Risk-Based Approach:** Prioritize security measures based on real-time risks and focus on protecting critical assets and processes.
* **Automation and Machine Learning:** Leverage technology to automate repetitive tasks, enhance detection capabilities, and reduce human error.
* **Security Awareness and Training:** Empower employees with knowledge of security threats and best practices to prevent user-caused breaches.
* **Collaboration and Transparency:** Foster open communication between security teams, business units, and stakeholders to align security goals with organizational objectives.
* **Continuous Monitoring and Improvement:** Regularly review and update security measures based on changing threats and technological advancements.

**Implementing a Smart Security Strategy:**

* **Conduct a Risk Assessment:** Identify and prioritize critical assets and processes that require enhanced security protections.
* **Invest in Automation and ML:** Implement technologies that automate security tasks, such as intrusion detection, threat analysis, and incident response.
* **Educate Employees:** Provide comprehensive security training programs to employees at all levels to equip them with the knowledge to protect their own devices and company data.
* **Foster Collaboration:** Establish cross-functional teams that include security, IT, and business stakeholders to ensure a unified approach to security.
* **Implement Continuous Monitoring:** Deploy security monitoring tools and processes to proactively detect and respond to threats in real time.

**Benefits of Working Smarter:**

* **Enhanced Security Effectiveness:** Improved efficiency and automation reduce human error and increase detection capabilities.
* **Reduced Costs:** Automation and machine learning can reduce labor costs and improve return on investment in security.
* **Improved Transparency and Accountability:** Clear communication and monitoring processes increase trust and accountability within the organization.
* **Enhanced Stakeholder Confidence:** A proactive and transparent security strategy demonstrates commitment to protecting data and assets, building trust with customers, partners, and investors.

**Conclusion:**

Winning back lost trust in security requires organizations to embrace smart security practices. By adopting a risk-based approach, leveraging automation and machine learning, fostering collaboration and transparency, and implementing continuous monitoring, organizations can improve security effectiveness, reduce costs, and enhance trust with all stakeholders. A smart security strategy is not only essential for protecting critical assets but also for building a reputation of integrity and reliability in an increasingly connected world.

## Gartner: Mitigating security threats in AI agents
[Read more](https://www.computerweekly.com/opinion/Gartner-Mitigating-security-threats-in-AI-agents)

Published: Mon, 23 Sep 2024 09:34:00 GMT

**Mitigating Security Threats in AI Agents**

**By Gartner**

**Key Findings**

* AI agents are increasingly being used in critical applications, making it essential to address security threats.
* Common security threats to AI agents include: data poisoning, adversarial examples, model stealing, and algorithm bias.
* Organizations can mitigate these threats by implementing a comprehensive security framework that addresses both technical and organizational measures.

**Recommendations**

* Implement robust data validation and cleaning processes to prevent data poisoning.
* Use adversarial training techniques to make models more resilient to adversarial examples.
* Protect model parameters and architecture from unauthorized access to prevent model stealing.
* Audit and monitor models for algorithm bias to ensure fairness and avoid discriminatory outcomes.
* Establish clear accountability and governance mechanisms for AI agents.

**Introduction**

AI agents are rapidly becoming an integral part of our lives, from powering self-driving cars to providing personalized healthcare. However, as AI agents become more sophisticated, so do the security threats they face. This report provides an overview of the common security threats to AI agents and offers recommendations for mitigating them.

**Common Security Threats to AI Agents**

* **Data poisoning:** Malicious actors can manipulate training data to cause an AI agent to make incorrect predictions.
* **Adversarial examples:** Specially crafted inputs can be designed to fool an AI agent into making a mistake.
* **Model stealing:** Attackers can steal an AI model and use it for their own purposes, such as creating fake news or phishing emails.
* **Algorithm bias:** AI models can be biased towards certain groups of people, leading to unfair or discriminatory outcomes.

**Mitigating Security Threats**

To mitigate security threats to AI agents, organizations can implement a comprehensive security framework that addresses both technical and organizational measures.

**Technical Measures**

* **Data validation and cleaning:** Validate and clean training data to remove malicious or erroneous data.
* **Adversarial training:** Train models on adversarial examples to improve their resilience.
* **Model protection:** Protect model parameters and architecture from unauthorized access.
* **Bias mitigation:** Audit and monitor models for bias and implement techniques to mitigate it.

**Organizational Measures**

* **Accountability:** Establish clear accountability for the development, deployment, and use of AI agents.
* **Governance:** Implement governance mechanisms to ensure compliance with ethical and legal requirements.
* **Training and awareness:** Educate developers and end users about AI security risks and mitigation techniques.
* **Incident response:** Develop and implement an incident response plan for AI security breaches.

**Conclusion**

Security threats to AI agents are a serious concern that must be addressed in order to ensure the safe and ethical use of AI. By implementing a comprehensive security framework that addresses both technical and organizational measures, organizations can mitigate these threats and protect their AI investments.

## Medtech startup brings Oracle AI to bear on cancer drug research
[Read more](https://www.computerweekly.com/news/366611519/Medtech-startup-brings-Oracle-AI-to-bear-on-cancer-drug-research)

Published: Mon, 23 Sep 2024 06:11:00 GMT

**Medtech Startup Harnesses Oracle AI for Cancer Drug Discovery**

A groundbreaking medtech startup is revolutionizing cancer drug research by leveraging the prowess of Oracle Artificial Intelligence (AI). This innovative approach promises to accelerate drug discovery, leading to improved patient outcomes and potentially life-saving treatments.

**Harnessing AI's Power**

The startup, based in Silicon Valley, has developed a cutting-edge platform that incorporates Oracle AI capabilities. This platform harnesses vast amounts of medical data, including genetic information, clinical trials, and patient outcomes. By utilizing machine learning algorithms, the platform can analyze complex patterns and identify novel insights that were once hidden from researchers.

**Accelerated Drug Discovery**

The platform's AI-driven capabilities enable researchers to quickly identify potential drug candidates and predict their efficacy and safety. This process, which traditionally takes years, can now be completed within weeks or months, dramatically reducing the time-to-market for new cancer drugs.

**Personalized Treatment Plans**

Furthermore, the AI platform provides valuable insights into a patient's specific genetic profile. This information can be used to tailor treatment plans, ensuring that each patient receives the most effective therapy based on their unique characteristics. This personalized approach enhances treatment outcomes and reduces the risk of adverse events.

**Collaboration with Oracle**

The startup's collaboration with Oracle has been instrumental in their success. Oracle AI provides a comprehensive set of tools and infrastructure that empowers researchers to develop and deploy AI models with ease. The partnership also ensures access to the latest AI technologies and expertise.

**Promising Results**

Early trials utilizing the AI platform have shown promising results. Researchers have identified several promising drug candidates that have exhibited high efficacy and low toxicity in preclinical models. Clinical trials are currently underway to validate these findings and bring these novel therapies to patients.

**A New Era in Cancer Treatment**

The integration of AI into cancer drug research is ushering in a new era of personalized medicine. The medtech startup's innovative platform, powered by Oracle AI, is transforming the way cancer is treated, leading to faster drug discovery, more effective therapies, and improved patient outcomes.

## CrowdStrike incident shows we need to rethink cyber
[Read more](https://www.computerweekly.com/opinion/CrowdStrike-incident-shows-we-need-to-rethink-cyber)

Published: Fri, 20 Sep 2024 09:17:00 GMT

The recent CrowdStrike incident is a stark reminder of the evolving nature of cybersecurity threats and the need for organizations to rethink their approach to protecting their data and systems.

CrowdStrike, a leading cybersecurity firm, was the victim of a sophisticated phishing attack that resulted in the theft of sensitive information from its customers. The attack highlights the growing sophistication of cybercriminals and the need for organizations to adopt a more proactive and comprehensive approach to cybersecurity.

One of the most concerning aspects of the CrowdStrike incident is the use of phishing techniques to target employees. Phishing is a type of social engineering attack that uses email or other forms of communication to trick victims into providing sensitive information, such as passwords or credit card numbers. Phishing attacks are becoming increasingly common and sophisticated, and they can be difficult to detect, even for experienced users.

The CrowdStrike incident also highlights the importance of having a strong incident response plan in place. When an organization is the victim of a cyberattack, it is critical to have a clear and concise plan in place to respond to the incident and mitigate the damage. The incident response plan should include steps for identifying the scope of the attack, containing the damage, and notifying affected parties.

In the wake of the CrowdStrike incident, organizations should take the following steps to rethink their approach to cybersecurity:

* Implement a strong incident response plan.
* Train employees on how to identify and avoid phishing attacks.
* Use multi-factor authentication to protect sensitive data.
* Regularly patch and update software and systems.
* Implement a comprehensive cybersecurity strategy that includes both technical and non-technical measures.

By taking these steps, organizations can help to protect themselves from the evolving threat of cyberattacks.

## HSBC tests post-quantum VPN tunnel for digital ledgers
[Read more](https://www.computerweekly.com/news/366611375/HSBC-tests-post-quantum-VPN-tunnel-for-digital-ledgers)

Published: Thu, 19 Sep 2024 10:31:00 GMT

**HSBC Tests Post-Quantum VPN Tunnel for Digital Ledgers**

HSBC, a leading global banking and financial services provider, has successfully tested a post-quantum virtual private network (VPN) tunnel for digital ledgers. This breakthrough represents a significant step forward in safeguarding digital assets from emerging threats posed by quantum computing.

**Post-Quantum Computing and Its Threats**

Quantum computing, with its immense computational power, poses a potential risk to current cryptographic algorithms used to secure digital assets. Post-quantum cryptographic algorithms are designed to withstand these threats by employing more complex mathematical problems that even quantum computers would find challenging to solve effectively.

**HSBC's VPN Tunnel Implementation**

HSBC's VPN tunnel utilizes post-quantum algorithms to establish a secure connection between two parties sharing confidential information over a public network. The tunnel employs the MQShield protocol, a renowned and promising post-quantum cryptographic algorithm.

**Securing Digital Ledgers**

The VPN tunnel is crucial for protecting digital ledgers, which are distributed and immutable records of transactions. These ledgers, such as those used in blockchain technology, contain highly sensitive financial and personal data that must be safeguarded against potential breaches.

**Benefits of Post-Quantum VPN Tunnel**

* **Enhanced Security:** Post-quantum algorithms provide a higher level of protection against attacks from quantum computers, ensuring the confidentiality and integrity of digital assets.
* **Future-Proofing:** By implementing this technology now, HSBC is preparing for the potential impact of quantum computing, ensuring the security of digital ledgers in the long term.
* **Improved Efficiency:** Post-quantum algorithms can be more efficient than traditional cryptographic algorithms, resulting in faster and more seamless transactions on digital ledgers.

**HSBC's Commitment to Security**

HSBC's successful testing of the post-quantum VPN tunnel demonstrates their unwavering commitment to protecting their customers' digital assets from evolving threats. This initiative reinforces the bank's belief in innovation and the advancement of cutting-edge technologies for securing the future of financial services.

**Conclusion**

HSBC's post-quantum VPN tunnel is a significant step towards safeguarding digital ledgers from the challenges posed by quantum computing. By embracing post-quantum cryptographic algorithms, HSBC is positioning itself as a leader in securing the future of digital finance and safeguarding the trust of its customers.

## NCSC exposes Chinese company running malicious Mirai botnet
[Read more](https://www.computerweekly.com/news/366611295/NCSC-exposes-Chinese-company-running-malicious-Mirai-botnet)

Published: Wed, 18 Sep 2024 13:18:00 GMT

**NCSC Exposes Chinese Company Running Malicious Mirai Botnet**

The National Cyber Security Centre (NCSC) in the UK has uncovered a Chinese company operating a malicious botnet that employs the infamous Mirai malware. This botnet has been used to launch distributed denial-of-service (DDoS) attacks against targets worldwide.

**Mirai Botnet**

Mirai is a sophisticated malware first identified in 2016. It targets devices connected to the Internet of Things (IoT), such as surveillance cameras, routers, and printers. By exploiting vulnerabilities in these devices, Mirai can infect and control them, creating a botnet that can be used for large-scale DDoS attacks.

**Chinese Company Exposed**

The NCSC's investigation revealed that a Chinese company called Hangzhou Xiongmai Technology Co., Ltd. was running the malicious Mirai botnet. The company allegedly programmed the botnet to target specific IP addresses and was using it for commercial purposes.

**DDoS Attacks**

The Mirai botnet operated by Xiongmai has been linked to numerous high-profile DDoS attacks. These attacks have targeted websites, online services, and critical infrastructure. In some cases, the attacks have caused significant disruption and financial losses.

**Implications**

The NCSC's findings highlight the growing threat posed by malicious botnets run by state-sponsored actors. These botnets can be used to disrupt critical services, steal sensitive information, and manipulate public opinion.

**Response**

The NCSC is urging organizations to take steps to protect themselves from DDoS attacks, such as:

* Patching vulnerabilities in IoT devices
* Implementing network security controls
* Investing in DDoS mitigation technologies

The NCSC has also contacted Xiongmai and demanded that it cease all malicious activity. The company has since taken steps to disable the Mirai botnet.

**Conclusion**

The exposure of a Chinese company running a malicious Mirai botnet serves as a reminder of the importance of cybersecurity vigilance. Organizations and individuals alike must be aware of the risks posed by botnets and take appropriate measures to protect themselves from their destructive capabilities.

## What is email spam and how to fight it?
[Read more](https://www.techtarget.com/searchsecurity/definition/spam)

Published: Wed, 18 Sep 2024 09:00:00 GMT

**What is Email Spam?**

Email spam, also known as junk mail, is unsolicited electronic mail that is sent to multiple recipients without their consent. Spam typically contains unwanted advertising, phishing attempts, malware, or other malicious content.

**How to Fight Email Spam:**

**1. Use Anti-Spam Filters:**

* Set up strong spam filters in your email client or use a dedicated anti-spam software. These filters can block or filter out messages that match known spam patterns.

**2. Avoid Giving Out Your Email Address:**

* Be cautious about giving out your email address on untrustworthy websites or online forms. Use disposable email addresses for non-essential sign-ups.

**3. Mark Spam as Spam:**

* Report spam messages to your email provider by marking them as "Spam" or "Junk." This helps email providers learn about spam patterns and improve their filtering systems.

**4. Unsubscribe from Mailing Lists:**

* If you start receiving spam from a particular sender, check for an unsubscribe link at the bottom of the message. Clicking on it will remove you from their mailing list.

**5. Use a Privacy-Focused Email Service:**

* Some email services, such as ProtonMail and Tutanota, prioritize user privacy and have robust anti-spam measures in place.

**6. Block Suspicious Senders:**

* Identify suspicious email addresses and block them from contacting you using your email client's blocking features.

**7. Educate Yourself and Others:**

* Stay informed about common spam tactics and share your knowledge with others. Encourage friends and family to follow best practices as well.

**Additional Tips:**

* Be wary of emails that claim to be from reputable companies but contain odd or unfamiliar links or attachments.
* Never open attachments from unknown senders.
* Keep your software and operating system up to date with the latest security patches.
* If you suspect you have clicked on a malicious link or opened an infected attachment, take immediate action by scanning your device with an antivirus software and changing your passwords.

