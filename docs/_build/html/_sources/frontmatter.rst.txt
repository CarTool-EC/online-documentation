|Un dibujo de una persona El contenido generado por IA puede ser
incorrecto.|

   **Interoperability Architecture Solutions**

**European Interoperability Reference Architecture Specification**

EIRA & eGovERA

   *Directorate-General for Informatics*

   Reference

   European Interoperability Reference Architecture Specification – EIRA
   and eGovERA v1.0.0

   Keywords

   <EIRA, eGovERA, ABBs, SBBs, Archimate, interoperability>

|image1|

**CHANGE CONTROL**

+---------------------------------+----------------------------------------------+
| **Modification**                | **Details**                                  |
+=================================+==============================================+
| **Version 1.0.0**                                                              |
+---------------------------------+----------------------------------------------+
| **Current version**             |                                              |
+---------------------------------+----------------------------------------------+

   **DISCLAIMER**

   The information and views set out in this publication are those of
   the author(s) and do not necessarily reflect the official opinion of
   the Commission. The Commission does not guarantee the accuracy of the
   data included in this document. Neither the Commission nor any person
   acting on the Commission’s behalf may be held responsible for the use
   which may be made of the information contained therein.

   © European Union, 2026

   **European Commission**

   Directorate-General for Informatics

   Directorate B – Digital Public Services, Unit B2 – Interoperability
   Unit Contact: Catalin Moruju – Project Officer for the
   Interoperability Architecture Action

   E-mail: Catalin.MORUJU@ec.europa.eu

   *European Commission B-1049 Brussels*

**Intellectual Property Rights:**

   The work is licensed under the European Union Public Licence (EUPL)
   v1.2. Reuse is authorised provided the source is acknowledged.

   The reuse policy of European Commission documents is regulated by
   Decision 2011/833/EU (OJ L 330, 14.12.2011, p. 39).

   **Foreword**

   This Specification has been produced by the Interoperability
   Architecture Solutions team, a Digital Europe (DEP) Programme
   initiative in alignment with the European Standardisation Regulation
   1025/2012

TABLE OF CONTENTS

`1. Introduction <#introduction>`__ `6 <#introduction>`__

`1.1. Purpose of this Specification <#purpose-of-this-specification>`__
`6 <#purpose-of-this-specification>`__

`1.2. Scope <#scope>`__ `7 <#scope>`__

`1.3. Target Audience <#target-audience>`__ `7 <#target-audience>`__

`1.4. Relationship to Other Frameworks and
Standards <#relationship-to-other-frameworks-and-standards>`__
`8 <#relationship-to-other-frameworks-and-standards>`__

`1.5. Document Conventions and
Terminology <#document-conventions-and-terminology>`__
`8 <#document-conventions-and-terminology>`__

`2. Conceptual Foundations <#_Toc223625389>`__ `11 <#_Toc223625389>`__

`2.1. The European Interoperability Reference Architecture,
EIRA© <#the-european-interoperability-reference-architecture-eira>`__
`11 <#the-european-interoperability-reference-architecture-eira>`__

`2.2. The eGovernment European Reference Architecture,
eGovERA© <#the-egovernment-european-reference-architecture-egovera>`__
`11 <#the-egovernment-european-reference-architecture-egovera>`__

`2.3. Purposes of EIRA and eGovERA <#purposes-of-eira-and-egovera>`__
`11 <#purposes-of-eira-and-egovera>`__

`2.3.1. Core Shared Purposes <#core-shared-purposes>`__
`11 <#core-shared-purposes>`__

`2.4. Unit of analysis <#unit-of-analysis>`__ `12 <#unit-of-analysis>`__

`2.5. Use cases for the Reference
Architectures <#use-cases-for-the-reference-architectures>`__
`13 <#use-cases-for-the-reference-architectures>`__

`2.6. The role of Architecture
Principles <#the-role-of-architecture-principles>`__
`13 <#the-role-of-architecture-principles>`__

`2.7. Diving into core components (ABBs, SBBs, views, and
viewpoints). <#diving-into-core-components-abbs-sbbs-views-and-viewpoints.>`__
`14 <#diving-into-core-components-abbs-sbbs-views-and-viewpoints.>`__

`2.8. The (EIRA) Ontology <#the-eira-ontology>`__
`15 <#the-eira-ontology>`__

`2.8.1. Purpose and Nature <#purpose-and-nature>`__
`15 <#purpose-and-nature>`__

`2.8.2. Analysis of an European public administration Interoperable
Solution <#analysis-of-an-european-public-administration-interoperable-solution>`__
`16 <#analysis-of-an-european-public-administration-interoperable-solution>`__

`2.8.3. Design of a European public administration Interoperable
Solution or Documentation of a existing European public administration
Interoperable
Solution <#design-of-a-european-public-administration-interoperable-solution-or-documentation-of-a-existing-european-public-administration-interoperable-solution>`__
`17 <#design-of-a-european-public-administration-interoperable-solution-or-documentation-of-a-existing-european-public-administration-interoperable-solution>`__

`2.9. Key Interoperability Enablers
(viewpoint) <#key-interoperability-enablers-viewpoint>`__
`17 <#key-interoperability-enablers-viewpoint>`__

`2.9.1. Purpose and Nature <#purpose-and-nature-1>`__
`17 <#purpose-and-nature-1>`__

`2.10. The RA and related standards and specifications (ArchiMate©,
PAAF) <#the-ra-and-related-standards-and-specifications-archimate-paaf>`__
`18 <#the-ra-and-related-standards-and-specifications-archimate-paaf>`__

`2.10.1. ArchiMate© and the RA <#archimate-and-the-ra>`__
`18 <#archimate-and-the-ra>`__

`2.10.2. PAAF and the RA <#paaf-and-the-ra>`__ `19 <#paaf-and-the-ra>`__

`3. Reference Architecture Views &
Viewpoints <#reference-architecture-views-viewpoints>`__
`22 <#reference-architecture-views-viewpoints>`__

`3.1. Views <#views>`__ `22 <#views>`__

`3.1.1. Legal view <#legal-view>`__ `22 <#legal-view>`__

`3.1.2. Organisational view <#organisational-view>`__
`23 <#organisational-view>`__

`3.1.3. Semantic view <#semantic-view>`__ `23 <#semantic-view>`__

`3.1.4. Technical view, Application and
Infrastructure <#technical-view-application-and-infrastructure>`__
`23 <#technical-view-application-and-infrastructure>`__

`3.2. Viewpoints <#viewpoints>`__ `24 <#viewpoints>`__

`3.2.1. Interoperability Dimensions
viewpoints <#interoperability-dimensions-viewpoints>`__
`24 <#interoperability-dimensions-viewpoints>`__

`3.2.2. Other viewpoints defined in
EIRA <#other-viewpoints-defined-in-eira>`__
`24 <#other-viewpoints-defined-in-eira>`__

`3.3. Views and viewpoints, differences and
purposes <#views-and-viewpoints-differences-and-purposes>`__
`25 <#views-and-viewpoints-differences-and-purposes>`__

`4. Architecture Building Blocks
(ABBs) <#architecture-building-blocks-abbs>`__
`27 <#architecture-building-blocks-abbs>`__

`4.1. Definition and role of Architecture Building
Blocks <#definition-and-role-of-architecture-building-blocks>`__
`27 <#definition-and-role-of-architecture-building-blocks>`__

`4.2. Relationships and Dependencies Between Architecture Building
Blocks <#relationships-and-dependencies-between-architecture-building-blocks>`__
`29 <#relationships-and-dependencies-between-architecture-building-blocks>`__

`5. Solution Building Blocks (SBBs) <#solution-building-blocks-sbbs>`__
`32 <#solution-building-blocks-sbbs>`__

`5.1. What are Solution Building Block in the
EIRA <#what-are-solution-building-block-in-the-eira>`__
`32 <#what-are-solution-building-block-in-the-eira>`__

`5.2. SBBs and standards or
specifications <#sbbs-and-standards-or-specifications>`__
`32 <#sbbs-and-standards-or-specifications>`__

`5.3. SBBs as COTS, OSS or complete
solutions <#sbbs-as-cots-oss-or-complete-solutions>`__
`33 <#sbbs-as-cots-oss-or-complete-solutions>`__

`6. Architecture Patterns & Case
Studies <#architecture-patterns-case-studies>`__
`36 <#architecture-patterns-case-studies>`__

`6.1. Architecture patterns <#architecture-patterns>`__
`36 <#architecture-patterns>`__

`6.2. The Domain Specific Reference Architectures: Health, Customs, and
Tax <#the-domain-specific-reference-architectures-health-customs-and-tax>`__
`36 <#the-domain-specific-reference-architectures-health-customs-and-tax>`__

`6.2.1. eGovERA Health Reference
Architecture <#egovera-health-reference-architecture>`__
`37 <#egovera-health-reference-architecture>`__

`6.2.2. eGovERA Customs Reference
Architecture <#egovera-customs-reference-architecture>`__
`37 <#egovera-customs-reference-architecture>`__

`6.2.3. eGovERA Tax Reference
Architecture <#egovera-tax-reference-architecture>`__
`37 <#egovera-tax-reference-architecture>`__

`6.3. Case studies, the Reference Architectures in
use <#case-studies-the-reference-architectures-in-use>`__
`37 <#case-studies-the-reference-architectures-in-use>`__

`6.3.1. eGovERA© success story on a Data Space and Linked Data in
Flanders <#egovera-success-story-on-a-data-space-and-linked-data-in-flanders>`__
`38 <#egovera-success-story-on-a-data-space-and-linked-data-in-flanders>`__

`6.3.2. eGovERA success on a Data Space with the Council of
Madrid <#egovera-success-on-a-data-space-with-the-council-of-madrid>`__
`38 <#egovera-success-on-a-data-space-with-the-council-of-madrid>`__

`6.3.3. eGovERA success on ViDA e invoicing requirements with DG
TAXUD <#egovera-success-on-vida-e-invoicing-requirements-with-dg-taxud>`__
`38 <#egovera-success-on-vida-e-invoicing-requirements-with-dg-taxud>`__

`6.3.4. First public procurement use case for EIRA and ITB with
CACSA <#first-public-procurement-use-case-for-eira-and-itb-with-cacsa>`__
`38 <#first-public-procurement-use-case-for-eira-and-itb-with-cacsa>`__

`7. Validation, Conformance & Compliance
Testing <#validation-conformance-compliance-testing>`__
`40 <#validation-conformance-compliance-testing>`__

`7.1. Distinguishing Validation, Conformance and Compliance
Testing <#distinguishing-validation-conformance-and-compliance-testing>`__
`40 <#distinguishing-validation-conformance-and-compliance-testing>`__

`7.1.1. Validation <#validation>`__ `40 <#validation>`__

`7.1.2. Conformance <#conformance>`__ `40 <#conformance>`__

`7.1.3. Compliance <#compliance>`__ `41 <#compliance>`__

`7.2. Conformance Levels <#conformance-levels>`__
`41 <#conformance-levels>`__

`7.2.1. Mandatory Conformance <#mandatory-conformance>`__
`41 <#mandatory-conformance>`__

`7.2.2. Recommended Conformance <#recommended-conformance>`__
`41 <#recommended-conformance>`__

`7.2.3. Optional Conformance <#optional-conformance>`__
`42 <#optional-conformance>`__

`7.3. Compliance Profiles <#compliance-profiles>`__
`42 <#compliance-profiles>`__

`7.3.1. Cross-Border Compliance
Profile <#cross-border-compliance-profile>`__
`42 <#cross-border-compliance-profile>`__

`7.3.2. Sector-Specific Compliance
Profile <#sector-specific-compliance-profile>`__
`42 <#sector-specific-compliance-profile>`__

`7.3.3. Organisational Compliance
Profile <#organisational-compliance-profile>`__
`42 <#organisational-compliance-profile>`__

`8. Governance & Lifecycle <#governance-lifecycle>`__
`45 <#governance-lifecycle>`__

`8.1. Maintenance and evolution of the Reference
Architecture <#maintenance-and-evolution-of-the-reference-architecture>`__
`45 <#maintenance-and-evolution-of-the-reference-architecture>`__

`8.1.1. Change Management process -
lifecycle <#change-management-process---lifecycle>`__
`45 <#change-management-process---lifecycle>`__

`8.1.2. Semantic versioning Scheme <#semantic-versioning-scheme>`__
`46 <#semantic-versioning-scheme>`__

`8.2. Maintaining and evolving the Reference Architecture
Specification <#maintaining-and-evolving-the-reference-architecture-specification>`__
`46 <#maintaining-and-evolving-the-reference-architecture-specification>`__

`8.3. Community feedback mechanisms <#community-feedback-mechanisms>`__
`47 <#community-feedback-mechanisms>`__

`8.3.1. The Interoperable Europe Portal
Collection <#the-interoperable-europe-portal-collection>`__
`47 <#the-interoperable-europe-portal-collection>`__

`8.3.2. The Interoperable Architecture Solutions GitHub
Space <#the-interoperable-architecture-solutions-github-space>`__
`48 <#the-interoperable-architecture-solutions-github-space>`__

`9. Appendices <#appendices>`__ `50 <#appendices>`__

`9.1. Glossary of Key Terms <#glossary-of-key-terms>`__
`50 <#glossary-of-key-terms>`__

`9.2. Abbreviations list <#abbreviations-list>`__
`50 <#abbreviations-list>`__

`9.3. Templates for ABB/SBB definition and capability
assessment. <#templates-for-abbsbb-definition-and-capability-assessment.>`__
`50 <#templates-for-abbsbb-definition-and-capability-assessment.>`__

`9.4. Reference Architecture Persistent URI
schema <#reference-architecture-persistent-uri-schema>`__
`54 <#reference-architecture-persistent-uri-schema>`__

`9.5. Normative References <#normative-references>`__
`54 <#normative-references>`__

`9.6. Non-Normative References <#non-normative-references>`__
`54 <#non-normative-references>`__

`9.7. Bibliographic References (Web, Documents, Books, Institutions,
etc) <#bibliographic-references-web-documents-books-institutions-etc>`__
`54 <#bibliographic-references-web-documents-books-institutions-etc>`__

|Dibujo de una persona El contenido generado por IA puede ser
incorrecto.|

   1

   Introduction