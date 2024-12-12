---
title: IT Security RSS Feed for 2024-12-10
date: 2024-12-10 02:31:38
tags: [RSS, ComputerWeekly, IT Security]
author: ComputerWeekly
summary: IT Security RSS Feed
lang: en
categories: IT Security
sitemap: true
comments: true
---

# IT Security RSS Feed for 2024-12-10

## In 2025: Identities conquer, and hopefully unite
[Read more](https://www.computerweekly.com/opinion/In-2025-Identities-conquer-and-hopefully-unite)

Published: Mon, 09 Dec 2024 14:10:00 GMT

**In 2025: Identities Conquer, and Hopefully Unite**

The year 2025 marks a turning point in human history, where identities transcend boundaries and become a catalyst for unity.

**The Rise of Intersectional Identities:**

Citizens no longer identify solely by one aspect of their identity. Instead, they embrace the complexities and intersections of their race, gender, sexual orientation, religion, and socioeconomic status. This interconnectedness fosters empathy and understanding, bridging divides that once separated communities.

**Identity as a Source of Empowerment:**

Individuals and groups are empowered by their identities. They use their voices and platforms to advocate for their rights and experiences, creating a more inclusive and just society. This empowerment challenges dominant narratives and amplifies marginalized perspectives.

**Technology Fosters Global Connections:**

Social media and other technologies connect people from diverse backgrounds, enabling them to share their stories, learn from each other, and build bridges across cultures. These connections break down stereotypes and promote cross-cultural understanding.

**Inclusive Policies and Institutions:**

Governments and institutions embrace the principles of intersectionality and inclusion. They implement policies and practices that recognize and value the diversity of identities, creating a level playing field for all citizens.

**The Challenge of Discrimination:**

Despite progress, discrimination remains a persistent challenge. However, the collective power of empowered identities and the support of allies create a strong force against hate and prejudice.

**A Path Towards Unity:**

The conquest of identities in 2025 represents a hopeful step towards unity. By embracing our differences and celebrating our common experiences, we create a society where everyone feels valued and connected.

**Conclusion:**

The year 2025 marks a transformative moment in human history, where identities become a source of empowerment and a pathway to unity. As we navigate the challenges of discrimination, we remain committed to building a just and equitable world where every individual can live their authentic self.

## AI and cloud: The perfect pair to scale your business in 2025
[Read more](https://www.computerweekly.com/opinion/AI-and-cloud-The-perfect-pair-to-scale-your-business-in-2025)

Published: Mon, 09 Dec 2024 14:01:00 GMT

**Unlocking Exponential Growth: AI and Cloud - The Dynamic Duo for Business Transformation**

The convergence of Artificial Intelligence (AI) and cloud computing is poised to revolutionize business landscapes in 2025 and beyond. This potent combination empowers organizations to scale unprecedentedly, drive innovation, and gain a competitive edge.

**Cloud Computing: The Foundation for AI's Success**

Cloud computing provides the scalable and cost-effective infrastructure essential for AI algorithms to operate. Its vast processing power, storage capacity, and advanced networking capabilities enable AI to handle massive datasets, train complex models, and provide real-time insights.

**AI: The Engine Driving Business Transformation**

AI algorithms can analyze data, identify patterns, and make predictions with astonishing accuracy. By leveraging AI, businesses can:

* **Automate processes:** Streamline repetitive tasks, reduce human error, and free up employees for more strategic endeavors.
* **Personalize experiences:** Tailor products, services, and marketing campaigns to individual customer needs.
* **Predict future trends:** Analyze historical data and identify emerging patterns to inform decision-making.
* **Enhance decision-making:** Provide data-driven insights to support informed decision-making at all levels of the organization.

**The Synergistic Impact of AI and Cloud**

Together, AI and cloud create a virtuous cycle that accelerates business performance. The cloud supports the deployment, training, and scaling of AI algorithms, while AI drives innovation and unlocks new business opportunities.

* **Increased Efficiency:** Automated processes and data-driven insights improve operational efficiency, reducing costs and increasing productivity.
* **Improved Customer Experience:** Personalized products, services, and interactions enhance customer satisfaction and loyalty.
* **Data-Driven Innovation:** AI algorithms generate insights that fuel new products, services, and market strategies.
* **Competitive Advantage:** By leveraging AI and cloud, businesses can differentiate themselves from competitors and gain a first-mover advantage.

**Case Studies: AI and Cloud in Action**

* **Tesla:** Uses AI to improve self-driving capabilities, enhancing safety and convenience for customers.
* **Spotify:** Personalizes music recommendations using AI, creating a tailored listening experience for each user.
* **Amazon:** Employs AI in inventory management and demand forecasting, optimizing supply chains and reducing waste.

**Conclusion**

In the fast-paced business environment of 2025, the convergence of AI and cloud is an indispensable tool for scaling growth. By harnessing the power of these technologies, organizations can unlock unprecedented efficiency, drive innovation, and establish themselves as industry leaders. Embracing this transformative duo is the key to unlocking the full potential of your business in the years to come.

## What is a session key?
[Read more](https://www.techtarget.com/searchsecurity/definition/session-key)

Published: Mon, 09 Dec 2024 09:00:00 GMT

A session key is a symmetric encryption key that is generated for use during a single communication session. It is used to encrypt and decrypt data that is exchanged between two or more parties during the session. Session keys are typically generated by a key exchange protocol, which is a cryptographic protocol that allows two parties to establish a shared secret key over an insecure channel.

Session keys are designed to provide confidentiality and integrity for the data that is exchanged during a session. They are typically used in conjunction with a session identifier, which is a unique value that is used to identify the session. The session identifier is typically included in the header of each message that is exchanged during the session.

Session keys are an important part of secure communication systems. They help to protect the confidentiality and integrity of data that is exchanged over insecure channels.

## What is cipher block chaining (CBC)?
[Read more](https://www.techtarget.com/searchsecurity/definition/cipher-block-chaining)

Published: Mon, 09 Dec 2024 09:00:00 GMT

**Cipher Block Chaining (CBC)** is a block encryption mode of operation that uses a cipher to encrypt a data block at a time, with each block being dependent on the previous one. Here's how CBC works:

**Initialization Vector (IV):**

* Before encryption, a random Initialization Vector (IV) is chosen. The IV is not encrypted but is included in the encrypted message.

**Encryption Process:**

* The data is divided into fixed-size blocks.
* The first data block (P1) is XORed with the IV and then encrypted using the cipher (C1 = E[IV XOR P1]).
* For subsequent data blocks (Pk), each block is XORed with the ciphertext of the previous block (Ck-1) before being encrypted (Ck = E[Ck-1 XOR Pk]).

**Decryption Process:**

* Decryption reverses the encryption process.
* The first ciphertext block (C1) is decrypted and XORed with the IV to recover the original data block (P1 = D[C1] XOR IV).
* For subsequent ciphertext blocks (Ck), each block is decrypted and XORed with the ciphertext of the previous block to recover the original data block (Pk = D[Ck] XOR Ck-1).

**Properties of CBC:**

* **Confidentiality:** CBC provides strong confidentiality by ensuring that each ciphertext block is dependent on the previous ones, making it difficult to infer information from intercepted ciphertext.
* **Integrity:** Alteration of any data block or ciphertext block will propagate through the subsequent blocks, making it easy to detect tampering.
* **Error Propagation:** Errors in transmission or storage can cause problems in decrypting blocks beyond the corrupted one.
* **Synchronization:** Loss of synchronization between the sender and receiver (e.g., due to lost packets) can disrupt decryption.

**Applications:**

CBC is widely used in applications requiring strong confidentiality and integrity, such as:

* Secure communications (e.g., TLS, VPNs)
* Data encryption in databases and file systems
* Password storage

## Bahrain faces legal action after planting Pegasus spyware on UK blogger
[Read more](https://www.computerweekly.com/news/366616823/Bahrain-faces-legal-action-after-planting-Pegasus-spyware-on-UK-blogger)

Published: Mon, 09 Dec 2024 06:00:00 GMT

**Background:**

* Sayed Ahmed Alwadaei, a Bahraini-British blogger and human rights activist, was targeted with Pegasus spyware in 2020.
* Pegasus, a highly sophisticated spyware developed by the Israeli company NSO Group, allows attackers to remotely access and monitor a target's device.
* Alwadaei alleges that his phone was hacked after downloading a link from a trusted contact.

**Legal Action:**

* In January 2023, Alwadaei and privacy organization Privacy International filed a lawsuit in the UK High Court against the government of Bahrain.
* The lawsuit accuses Bahrain of:
    * Installing Pegasus spyware on Alwadaei's phone without his consent.
    * Using Pegasus to monitor his communications and access his personal information.
    * Violating his privacy and freedom of expression rights.

**Allegations:**

* Alwadaei claims that Pegasus was used by Bahraini authorities to track his movements, record his conversations, and access his emails and social media accounts.
* He believes the surveillance was politically motivated due to his criticism of the Bahraini government's human rights record.
* Privacy International alleges that Bahrain has used Pegasus extensively to target activists, journalists, and dissidents.

**Response from Bahrain:**

* The Bahraini government has denied the allegations, stating that it does not use Pegasus spyware.
* It has accused Alwadaei of being a "terrorist" and has labeled Privacy International as a "pro-Iranian organization."

**Implications:**

* The lawsuit is a significant legal challenge against the alleged misuse of Pegasus spyware by a government.
* It raises concerns about the growing use of such surveillance technologies to silence dissent and violate human rights.
* The outcome of the case could have implications for the regulation of spyware and the protection of privacy and freedom of expression.

**Ongoing Developments:**

* The case is still ongoing, and a trial date has yet to be set.
* Privacy International has called for an independent investigation into Bahrain's use of Pegasus spyware.
* Alwadaei has expressed fears for his safety and has requested protection from the UK government.

## Six trends that will define cyber through to 2030
[Read more](https://www.computerweekly.com/opinion/Six-trends-that-will-define-cyber-through-to-2030)

Published: Fri, 06 Dec 2024 16:45:00 GMT

**1. The Convergence of Physical and Digital Worlds:**

* Cyber-physical systems (CPS) will seamlessly connect physical assets, devices, and processes with digital networks, creating interconnected and intelligent environments.

**2. Artificial Intelligence (AI) and Machine Learning (ML) Proliferation:**

* AI and ML algorithms will be extensively deployed for threat detection, prediction, and response, enhancing cybersecurity effectiveness.

**3. Quantum Computing's Impact:**

* Quantum computers will possess unprecedented computational power, potentially disrupting encryption and cryptography, requiring proactive countermeasures.

**4. Cybersecurity as a Shared Responsibility:**

* Governments, businesses, and individuals will collaborate more closely to address the growing cyberthreat landscape, recognizing the interconnected nature of cybersecurity.

**5. Cyber Insurance and Risk Management:**

* Cyber insurance will become increasingly prevalent as organizations seek to mitigate financial losses from cyber incidents, driving a focus on risk management and preparedness.

**6. Cybersecurity Talent Gap and Workforce Development:**

* The shortage of skilled cybersecurity professionals will remain a significant challenge, necessitating investments in training and education programs to develop the next generation of cyber experts.

## US TikTok ban imminent after appeal fails
[Read more](https://www.computerweekly.com/news/366616902/US-TikTok-ban-imminent-after-appeal-fails)

Published: Fri, 06 Dec 2024 14:38:00 GMT

**US TikTok ban imminent after appeal fails**

A federal appeals court has upheld a lower court ruling that would have banned TikTok from operating in the United States. The ban was scheduled to take effect on September 20, but TikTok filed an emergency appeal, which was denied by the appeals court.

The ban stems from a lawsuit filed by the Trump administration, which argued that TikTok posed a national security threat because it could be used by the Chinese government to collect data on American users. TikTok has denied these allegations, saying that it is an independent company and that it does not share user data with the Chinese government.

The appeals court ruled that the Trump administration had provided sufficient evidence to support its national security concerns. The court also said that TikTok had not shown that the ban would cause irreparable harm to the company.

TikTok has said that it will continue to fight the ban, and that it is confident that it will ultimately prevail. However, the appeals court's ruling is a major setback for the company, and it is unclear whether it will be able to continue operating in the United States.

If TikTok is banned, it would be a major blow to the company, which has become one of the most popular social media platforms in the world. TikTok has over 800 million active users, and it is particularly popular among young people.

The ban would also have a significant impact on the US economy. TikTok is a major employer, and it generates billions of dollars in revenue each year. The ban would also hurt businesses that rely on TikTok to reach their customers.

The Trump administration's decision to ban TikTok has been met with criticism from both Democrats and Republicans. Critics argue that the ban is politically motivated and that it will harm US businesses and consumers.

It is unclear what the future holds for TikTok in the United States. The company has said that it will continue to fight the ban, but it is unclear whether it will be successful. If the ban is upheld, it would be a major blow to TikTok and to the US economy.

## How AI can help you attract, engage and retain the best talent in 2025
[Read more](https://www.computerweekly.com/opinion/How-AI-can-help-you-attract-engage-and-retain-the-best-talent-in-2025)

Published: Fri, 06 Dec 2024 13:46:00 GMT

**Attracting Top Talent**

* **Personalized Candidate Outreach:** AI-powered platforms can analyze candidate data, identify suitable profiles, and generate personalized outreach messages to attract top talent.
* **Virtual Interviewing:** AI chatbots can conduct initial screening interviews, saving time for recruiters and providing a more efficient and convenient experience for candidates.
* **Predictive Hiring Algorithms:** AI algorithms can analyze past hiring data and candidate attributes to predict the success of potential candidates, reducing the risk of making poor hiring decisions.

**Engaging Employees**

* **AI-Powered Training and Development:** AI can create personalized learning paths tailored to individual employee needs and interests, increasing engagement and skill development.
* **Virtual Assistant Support:** AI virtual assistants can assist employees with routine tasks, freeing up their time for more strategic initiatives and improving overall work satisfaction.
* **Performance Monitoring and Feedback:** AI can analyze employee performance data and provide real-time feedback, helping managers identify development areas and support employee growth.

**Retaining Top Performers**

* **AI-Driven Retention Strategies:** AI algorithms can identify employees at risk of leaving and provide targeted interventions, such as personalized compensation packages or career growth opportunities.
* **Predictive Analytics for Turnover:** AI can predict the likelihood of employee turnover and identify contributing factors, allowing HR to implement proactive retention strategies.
* **AI-Powered Employee Engagement Surveys:** AI can analyze employee survey data in real-time, providing insights into areas for improvement and helping HR address employee concerns quickly.

**Additional Benefits**

* **Improved Diversity and Inclusion:** AI can help eliminate biases in hiring and reduce representation gaps by providing unbiased candidate assessments.
* **Enhanced Productivity and Innovation:** AI-powered tools can automate tasks, free up employee time, and foster innovation by providing access to insights and data.
* **Cost Savings:** AI can reduce manual labor costs associated with recruiting, candidate screening, and employee management, resulting in significant cost savings.

**Considerations**

* **Ethical Use of AI:** It's crucial to use AI ethically and ensure that it aligns with the organization's values and legal requirements.
* **Data Privacy and Security:** AI algorithms rely on data, so it's essential to implement robust data protection measures to ensure employee privacy.
* **Continuous Learning and Improvement:** AI is rapidly evolving, so organizations should invest in ongoing training and development to stay abreast of advancements in AI technology.

## TfL cyber attack cost over £30m to date
[Read more](https://www.computerweekly.com/news/366616875/TfL-cyber-attack-cost-over-30m-to-date)

Published: Fri, 06 Dec 2024 10:36:00 GMT

**TfL Cyber Attack Costs Soar Over £30m**

Transport for London (TfL) has confirmed that the recent cyber attack on its systems has cost the organization over £30 million to date. The attack, which took place in August 2022, disrupted multiple TfL services, including the Oyster card system and the TfL website.

The vast majority of the costs incurred have been for recovery and remediation activities, such as restoring damaged systems and implementing additional security measures. TfL has also incurred costs related to legal and insurance expenses, as well as business continuity measures.

The attack has had a significant impact on TfL's operations and finances. The disruption of the Oyster card system, which handles over 80% of journeys on the network, caused significant inconvenience to passengers and resulted in a loss of revenue for TfL.

TfL has launched an internal investigation into the attack and has been working closely with law enforcement agencies to identify the perpetrators. However, the investigation is still ongoing, and no arrests have been made at this time.

The attack has raised concerns about the resilience of public transport systems to cyber threats. TfL has pledged to strengthen its cybersecurity measures to prevent similar incidents in the future.

## What are Common Criteria (CC) for Information Technology Security Evaluation?
[Read more](https://www.techtarget.com/whatis/definition/Common-Criteria-CC-for-Information-Technology-Security-Evaluation)

Published: Thu, 05 Dec 2024 13:20:00 GMT

**Common Criteria (CC) for Information Technology Security Evaluation**

The Common Criteria (CC) is an internationally recognized set of security evaluation criteria used to assess the security capabilities of IT products. It provides a standardized framework for evaluating and validating the security of IT systems and products.

**Key Principles of CC:**

* **Protection Profile (PP):** Defines the security requirements that a product must meet.
* **Security Target (ST):** Describes how a product meets the security requirements defined in the PP.
* **Evaluation Report (ER):** Documents the results of the security evaluation conducted by an accredited evaluation laboratory.
* **Certification:** Grants a product a level of assurance based on the results of the evaluation.

**Levels of Assurance:**

CC defines six levels of assurance (EAL) for security evaluations:

* **EAL1:** Functional Testing
* **EAL2:** Structural Testing
* **EAL3:** Methodical Testing and Review
* **EAL4:** Limited Design Verification
* **EAL5:** Semi-Formal Design Verification
* **EAL6:** Formal Design Verification

**Evaluation Process:**

The CC evaluation process involves:

* **PP and ST Development:** Developing a PP that defines the security requirements and a ST that describes how a product meets these requirements.
* **Evaluation:** Conducting a security evaluation by an accredited laboratory to verify the product's compliance with the ST.
* **Certification:** Granting the product a level of assurance based on the evaluation results.

**Benefits of CC:**

* **Standardization:** Provides a common framework for evaluating IT security.
* **Assurance:** Grants a level of assurance about the security of a product.
* **Global Recognition:** Accepted by governments and organizations worldwide.
* **Trustworthiness:** Helps build trust in IT systems and products.
* **Security Enhancements:** Identifies areas for security improvement in products.

**Applications of CC:**

CC is used in various industries and applications, including:

* Government systems
* Payment systems
* Healthcare systems
* Industrial control systems
* Telecommunications networks
* Cloud computing environments

## Government agencies urged to use encrypted messaging after Chinese Salt Typhoon hack
[Read more](https://www.computerweekly.com/news/366616972/Government-agencies-urged-to-use-encrypted-messaging-after-Chinese-Salt-Typhoon-hack)

Published: Thu, 05 Dec 2024 12:30:00 GMT

**Government Agencies Advised to Deploy Encrypted Messaging Amidst Chinese Salt Typhoon Hack**

Government agencies have been strongly advised to implement encrypted messaging systems in the wake of a significant cyberattack perpetrated by Chinese threat actors. The attack, known as Salt Typhoon, exploited vulnerabilities in unencrypted messaging applications to steal sensitive information and disrupt critical infrastructure.

* **Background of the Salt Typhoon Hack:**
   * Salt Typhoon is a sophisticated cyberespionage campaign linked to Chinese state-sponsored actors.
   * The attack targeted government agencies, military organizations, and defense contractors worldwide.
   * Threat actors exploited unencrypted messaging apps to gain access to sensitive communications.

* **Urgency of Encryption:**
   * Government agencies possess vast amounts of sensitive and critical information.
   * Unencrypted messaging systems are a major vulnerability that can be easily exploited by malicious actors.
   * Encrypted messaging ensures the confidentiality and integrity of communications, protecting against unauthorized access.

* **Recommendations for Government Agencies:**
   * Implement end-to-end encryption for all messaging platforms used by government employees.
   * Conduct regular security audits to identify and mitigate vulnerabilities in messaging systems.
   * Train employees on the importance of cybersecurity best practices and the risks of unsecured messaging.

* **Benefits of Encrypted Messaging:**
   * Protects sensitive communications from interception and disclosure by unauthorized parties.
   * Prevents data breaches and the compromise of critical infrastructure.
   * Maintains trust and credibility among government stakeholders.

Government agencies must prioritize the implementation of encrypted messaging systems as a fundamental cybersecurity measure. The Salt Typhoon hack serves as a stark reminder of the risks posed by unencrypted communications and the need for robust security protocols to safeguard sensitive information. By embracing encryption, agencies can strengthen their cybersecurity posture and protect their critical assets from cyber threats.

## Are you on the naughty or nice list for responsible AI adoption?
[Read more](https://www.computerweekly.com/opinion/Are-you-on-the-naughty-or-nice-list-for-responsible-AI-adoption)

Published: Thu, 05 Dec 2024 10:03:00 GMT

**Nice List:**

* **Embracing Transparency**: Openly sharing AI algorithms, processes, and decisions to build trust and accountability.
* **Prioritizing Fairness and Inclusivity**: Ensuring that AI systems are unbiased, equitable, and avoid perpetuating societal biases.
* **Establishing Clear Ethical Guidelines**: Developing and implementing principled AI frameworks that guide decision-making.
* **Promoting Human-Centered AI**: Designing AI systems that augment human capabilities, enhance safety, and improve well-being.
* **Investing in Education and Upskilling**: Empowering stakeholders with the knowledge and skills needed to understand and engage with responsible AI.
* **Fostering Collaboration and Dialogue**: Engaging with diverse experts, policymakers, and the public to shape responsible AI practices.
* **Establishing Robust Governance Structures**: Implementing accountability mechanisms, oversight bodies, and external audits to ensure responsible AI adoption.

**Naughty List:**

* **Lack of Transparency**: Concealing AI algorithms and decision-making processes, leading to opacity and distrust.
* **Perpetuating Biases**: Building AI systems that amplify existing societal biases, resulting in unfair or discriminatory outcomes.
* **Ignoring Ethical Considerations**: Failing to address the ethical implications of AI technology, leading to potential harm or unintended consequences.
* **Overselling Capabilities**: Promising unrealistic benefits from AI, leading to disillusionment and mistrust.
* **Insufficient Investment in Education**: Neglecting to equip stakeholders with the necessary knowledge to responsibly engage with AI.
* **Lack of Collaboration and Dialogue**: Operating in isolation, missing out on valuable insights and best practices.
* **Inadequate Governance Structures**: Failing to implement effective accountability mechanisms and oversight bodies, leading to unchecked AI development.

## Shared digital gateway was source of three NHS ransomware attacks
[Read more](https://www.computerweekly.com/news/366616832/Shared-digital-gateway-was-source-of-three-NHS-ransomware-attacks)

Published: Wed, 04 Dec 2024 17:33:00 GMT

A shared digital gateway was the source of three ransomware attacks on NHS trusts, an investigation has found.

The attacks, which took place in May 2021, affected University Hospitals of Leicester NHS Trust, Sherwood Forest Hospitals NHS Foundation Trust and Barnsley Hospital NHS Foundation Trust.

The investigation, carried out by the National Cyber Security Centre (NCSC), found that the trusts were all using a shared digital gateway, which allowed them to connect to a variety of NHS systems.

The attackers were able to exploit a vulnerability in the gateway to gain access to the trusts' networks. They then encrypted files on the trusts' systems, demanding a ransom payment in order to decrypt them.

The NCSC said that the attacks were "sophisticated and targeted", and that the attackers had "significant knowledge" of the NHS's systems.

The NCSC also found that the trusts had not taken all the necessary steps to protect their systems from attack. For example, they had not implemented multi-factor authentication, which would have made it harder for the attackers to access their networks.

The NCSC has made a number of recommendations to the NHS to help prevent similar attacks in the future. These include:

* Implementing multi-factor authentication
* Patching systems regularly
* Backing up data regularly
* Training staff on cybersecurity awareness

The NHS has accepted the NCSC's recommendations and is working to implement them.

The ransomware attacks on the NHS are a reminder of the importance of cybersecurity. Healthcare organisations need to take all the necessary steps to protect their systems from attack. This includes implementing strong security measures and training staff on cybersecurity awareness.

## NCA takes out network that laundered ransomware payments
[Read more](https://www.computerweekly.com/news/366616657/NCA-takes-out-network-that-laundered-ransomware-payments)

Published: Wed, 04 Dec 2024 15:44:00 GMT

**National Crime Agency (NCA) Takes Down Network Laundering Ransomware Payments**

The National Crime Agency (NCA) has successfully dismantled a network responsible for laundering millions of pounds derived from ransomware attacks. The operation seized assets worth approximately £5 million.

**Modus Operandi:**

The network operated through a network of shell companies, cryptocurrency exchanges, and bank accounts. They laundered funds through a complex process involving multiple transfers and conversions to make it difficult to trace the origins of the money.

**Targets:**

The network targeted businesses and organizations worldwide with ransomware attacks, encrypting their data and demanding payment in cryptocurrency. Victims were often unable to recover their data without paying the ransom.

**Operation:**

The NCA worked in collaboration with law enforcement agencies in the United States, Canada, and Europol to dismantle the network. Investigators followed the money trail and identified the individuals involved.

**Arrests and Seizures:**

In a series of raids, the NCA arrested 17 individuals suspected of being involved in the network. They also seized computers, mobile phones, and documents.

**Impact:**

The NCA estimates that the network laundered over £100 million in ransomware proceeds. The operation has significantly disrupted the network and prevents them from continuing their activities.

**Statement from NCA:**

NCA Director General Graeme Biggar said, "This is a major success for the NCA and our international partners. Ransomware is a serious threat to businesses and organizations, and we are determined to do everything we can to disrupt the criminal gangs behind it."

**Significance:**

This operation demonstrates the NCA's commitment to combating cybercrime and its focus on disrupting the financial infrastructure used by criminals. It also serves as a warning to individuals involved in ransomware attacks that they will be prosecuted.

## The most pressing challenges for CISOs and cyber security teams
[Read more](https://www.computerweekly.com/opinion/The-most-pressing-challenges-for-CISOs-and-cyber-security-teams)

Published: Wed, 04 Dec 2024 12:32:00 GMT

**1. Rapidly Evolving Cyber Threat Landscape:**

* Constant emergence of new attack vectors and malware
* Sophisticated cybercriminal groups adopting advanced techniques
* Ransomware, phishing, and social engineering attacks on the rise

**2. Cloud Security and Data Protection:**

* Growing adoption of cloud computing raises concerns about data security
* Managing and securing data across multiple cloud platforms
* Complying with data privacy regulations

**3. Remote Work and Mobile Device Management:**

* Remote workforces create new attack surfaces
* Securing and managing employee-owned devices
* Preventing insider threats and data exfiltration

**4. Cryptocurrency and Blockchain Security:**

* Cryptocurrency theft and ransomware attacks
* Securing blockchain networks and digital wallets
* Managing the risks associated with cryptocurrency investments

**5. Artificial Intelligence (AI) Security:**

* AI-powered cyberattacks becoming increasingly sophisticated
* Defending against adversarial AI and deepfake technologies
* Ethical considerations and potential misuse of AI in cybersecurity

**6. Supply Chain Security:**

* Vulnerabilities in third-party vendors and partners
* Managing the risks of cyberattacks targeting the supply chain
* Ensuring supply chain resilience and continuity

**7. Ransomware and Business Continuity:**

* Ransomware attacks causing significant financial and reputational damage
* Developing comprehensive ransomware response and recovery plans
* Investing in business continuity measures to minimize downtime

**8. Shortage of Skilled Cybersecurity Professionals:**

* Growing demand for cybersecurity professionals
* Difficulty attracting and retaining qualified talent
* Addressing the skills gap to meet the increasing cybersecurity threats

**9. Regulatory and Compliance Pressure:**

* Increasing regulatory requirements for cybersecurity and data protection
* Complex compliance frameworks and evolving standards
* Managing the risk of fines and legal liability

**10. Strategic Alignment with Business Objectives:**

* Aligning cybersecurity strategies with business goals and priorities
* Demonstrating the value of cybersecurity investments
* Ensuring that cybersecurity supports business growth and innovation

## Nordics move to deepen cyber security cooperation
[Read more](https://www.computerweekly.com/news/366616450/Nordics-move-to-deepen-cyber-security-cooperation)

Published: Wed, 04 Dec 2024 08:25:00 GMT

The Nordic countries are moving to deepen their cooperation on cyber security, in response to the growing threat of cyber attacks.

The move comes as the region faces an increasing number of cyber attacks, targeting both government and private sector organisations. In recent months, several high-profile cyber attacks have hit Nordic countries, including the attack on the Danish government in December 2021.

In response to this growing threat, the Nordic countries have agreed to establish a new cyber security centre, which will be based in Finland. The centre will provide a platform for Nordic countries to share information and best practices on cyber security, and to coordinate their response to cyber attacks.

The centre will be staffed by experts from each of the Nordic countries, and will work closely with law enforcement and intelligence agencies. It will also provide training and support to Nordic governments and businesses on cyber security.

The establishment of the cyber security centre is a significant step forward in the Nordic countries' efforts to combat cyber attacks. The centre will provide a valuable platform for Nordic countries to share information and best practices, and to coordinate their response to cyber attacks.

The Nordic countries are not the only ones to be stepping up their efforts to combat cyber attacks. In recent years, there has been a growing global recognition of the threat posed by cyber attacks, and a number of countries have established cyber security centres or agencies.

## US updates telco security guidance after mass Chinese hack
[Read more](https://www.computerweekly.com/news/366616446/US-updates-telco-security-guidance-after-mass-Chinese-hack)

Published: Tue, 03 Dec 2024 15:05:00 GMT

**US Updates Telco Security Guidance After Mass Chinese Hack**

The Cybersecurity and Infrastructure Security Agency (CISA) has issued new security guidance for telecommunications companies following a massive hack that targeted telecom networks worldwide.

**Background on the Hack**

In December 2022, a Chinese state-sponsored cyberattack group known as APT41 compromised the networks of multiple telecommunications companies in the United States and other countries. The attackers gained access to sensitive information, including customer data, call records, and network configurations.

**CISA's New Guidance**

The new guidance provides recommendations for telecommunications companies to enhance their security posture and mitigate the risks of similar attacks. Key recommendations include:

* Implement multi-factor authentication (MFA) for all remote access points.
* Enforce strong password policies and regularly change passwords.
* Segment networks to limit the spread of any potential infection.
* Implement intrusion detection and prevention systems (IDPS) to identify and block malicious activity.
* Conduct regular security audits and penetration testing to identify vulnerabilities.
* Establish incident response plans and train staff on their implementation.

**Importance of the Guidance**

The telecom industry plays a critical role in modern society by providing essential communication services. As a result, it is a tempting target for cyberattacks, especially from state-sponsored actors like China.

The new CISA guidance aims to help telecommunications companies strengthen their defenses against these sophisticated threats. By implementing the recommendations, companies can reduce the risk of breaches, protect customer data, and ensure the integrity of their networks.

**Next Steps**

Telecommunications companies are encouraged to review the CISA guidance and begin implementing the recommended security measures. They should also continue to monitor the threat landscape and make adjustments to their security posture as needed.

By following these guidelines, telecommunications companies can help protect themselves and their customers from the growing threat of cyberattacks.

## F1 heightens fan experiences with the power of Salesforce
[Read more](https://www.computerweekly.com/news/366616475/F1-heightens-fan-experiences-with-the-power-of-Salesforce)

Published: Tue, 03 Dec 2024 11:50:00 GMT

**F1 Heightens Fan Experiences with the Power of Salesforce**

Formula One (F1) has transformed its fan experiences by leveraging the capabilities of Salesforce. Here's how:

**1. Personalized Fan Engagement:**

* Salesforce's Customer Relationship Management (CRM) platform allows F1 to track and analyze fan interactions across multiple channels (email, social media, etc.).
* This data enables F1 to create tailored content and promotions that align with individual fan preferences and past behaviors.

**2. Real-Time Race Insights:**

* F1 uses Salesforce to deliver real-time race data to fans on its mobile app and website.
* Fans can track the progress of drivers, monitor race statistics, and receive personalized updates based on their favorite teams and drivers.

**3. Enhanced Ticketing and Merchandise Sales:**

* Salesforce's e-commerce capabilities streamline ticket sales and merchandise purchases.
* Fans can easily access race information, select seats, and complete transactions seamlessly.

**4. Community Building:**

* F1 has created online fan communities powered by Salesforce's Community Cloud.
* These communities provide a platform for fans to connect, share race insights, and engage with F1 experts and influencers.

**5. Data-Driven Decision Making:**

* Salesforce's analytics dashboards provide F1 with insights into fan demographics, engagement patterns, and purchasing habits.
* This data enables F1 to optimize its marketing campaigns, content strategy, and overall fan experience.

**Benefits of Salesforce Implementation:**

* **Increased Fan Engagement:** Personalized content and real-time insights enhance fan satisfaction and loyalty.
* **Enhanced Revenue Generation:** Streamlined ticketing and merchandise sales drive revenue growth.
* **Improved Operational Efficiency:** Automated processes and centralized data streamline operations and reduce costs.
* **Data-Driven Insights:** Salesforce analytics empower F1 to make informed decisions based on fan behavior.
* **Competitive Advantage:** F1's innovative use of Salesforce sets it apart from other motorsports organizations and drives fan engagement.

In conclusion, F1's partnership with Salesforce has revolutionized its fan experiences. By leveraging the power of CRM, real-time data, and community building, F1 has created a connected and engaging experience that enhances fan enthusiasm and drives revenue growth.

## AIOps and storage management: What it is and who provides it
[Read more](https://www.computerweekly.com/feature/AIOps-and-storage-management-What-it-is-and-who-provides-it)

Published: Tue, 03 Dec 2024 07:00:00 GMT

**AIOps and Storage Management**

AIOps (Artificial Intelligence for IT Operations) is a combination of AI and machine learning (ML) techniques applied to IT operations to automate tasks, improve efficiency, and optimize performance. In the context of storage management, AIOps involves leveraging AI/ML to monitor, analyze, and optimize storage systems to enhance their performance, reliability, and efficiency.

**Benefits of AIOps for Storage Management**

* **Improved monitoring and analytics:** AIOps collects and analyzes a wide range of data from storage devices and systems, providing real-time insights into their performance and utilization.
* **Predictive maintenance:** AIOps uses ML algorithms to identify potential issues before they occur, allowing for proactive maintenance and minimizing downtime.
* **Automated resource allocation:** AIOps can optimize resource allocation by analyzing usage patterns and predicting future needs, ensuring efficient storage capacity utilization.
* **Reduced operational costs:** By automating tasks and improving efficiency, AIOps can significantly reduce operational costs associated with storage management.
* **Enhanced data security:** AIOps can detect and respond to security threats and anomalies in storage systems, improving data protection and compliance.

**Who Provides AIOps for Storage Management**

Several vendors provide AIOps solutions for storage management, including:

* **Dell Technologies:** Dell EMC AIOps for Storage Management
* **IBM:** IBM Storage Insights with AIOps
* **NetApp:** NetApp AIQ for Storage
* **Oracle:** Oracle Intelligent Storage Guardian
* **Pure Storage:** Pure1
* **VMware:** VMware vRealize Operations for Storage

**Key Considerations when Choosing an AIOps Solution**

When selecting an AIOps solution for storage management, consider the following factors:

* System compatibility
* Monitoring capabilities
* Analytics and reporting features
* Predictive maintenance and automation capabilities
* User interface and ease of use
* Integration with existing management tools
* Vendor support and pricing

## VMware ‘shock’ spawned lock-in rebellion, says NetApp
[Read more](https://www.computerweekly.com/news/366616595/VMware-shock-has-led-to-lock-in-rebellion-says-NetApp)

Published: Tue, 03 Dec 2024 05:19:00 GMT

**VMware ‘Shock’ Spawned Lock-In Rebellion, Says NetApp**

In an interview with CRN, NetApp CEO George Kurian claimed that VMware's recent price increases and licensing changes have sparked a "rebellion" among customers against vendor lock-in.

**Key Points:**

* Kurian stated that VMware's actions have "awakened" customers to the risks of vendor lock-in and the need for multi-vendor environments.
* He noted that NetApp has seen an increase in demand for its HCI solutions, which offer an alternative to VMware's offerings with more flexibility and lower costs.
* Kurian emphasized the benefits of open platforms and the need for vendors to give customers choice and control over their infrastructure.
* He said that NetApp is investing heavily in its own HCI and data fabric offerings to provide customers with a comprehensive alternative to VMware.

**Implications:**

* VMware's pricing and licensing changes have caused some customers to reconsider their reliance on the vendor.
* NetApp is capitalizing on this opportunity by offering customers an alternative HCI solution with more flexibility and lower costs.
* The incident highlights the increasing importance of multi-vendor environments and the demand for choice and control in cloud and data center infrastructures.

**Quotes:**

* **George Kurian, CEO, NetApp:** "VMware's shock to the market has really awakened customers to the risks of vendor lock-in. They're demanding multi-vendor environments, and they're looking for choice and control over their infrastructure."
* **Tom Wallack, Systems Engineer, CRN:** "Kurian's comments underscore the growing frustration among VMware customers over pricing and licensing changes. Customers are looking for alternatives, and NetApp is well-positioned to benefit from that."

**Conclusion:**

The "shock" caused by VMware's price increases and licensing changes has prompted a re-evaluation of vendor lock-in among customers. NetApp is leveraging this opportunity to offer an alternative HCI solution that provides more flexibility and lower costs, potentially challenging VMware's dominance in the market.

