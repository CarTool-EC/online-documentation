Architecture Patterns & Case Studies
====================================

This section complements the structural description of the European
Interoperability Reference Architecture (EIRA) by illustrating how its
architectural concepts are applied in practice. It introduces a set of
common interoperability patterns, domain-specific use cases, and
concrete case studies drawn from real deployments.

The objective is twofold: first, to demonstrate how recurring
interoperability challenges can be addressed through reusable
architectural approaches; and second, to show how EIRA and its extension
through eGovERA support the consistent realisation of these approaches
across policy domains and levels of government.

By linking abstract Architecture Building Blocks (ABBs) and Enablers to
Solution Building Blocks (SBBs) and operational solutions, this section
supports the understanding of practitioners in translating architectural
guidance into implementable designs while fostering reuse, alignment,
and interoperability by design.

Architecture patterns
---------------------

Interoperability patterns describe recurrent architectural solutions to
common interoperability needs observed across public sector systems.
Rather than prescribing specific technologies, these patterns define
stable combinations of responsibilities, interactions, and constraints
that can be realised through different implementations.

Following, some cases that EIRA and eGovERA cover, **these are not the
only patterns**, but rather, **examples**:

- **Federated Identity and Access Management**. This pattern addresses
  cross-organisational and cross-border authentication and
  authorisation. In EIRA, it relies on identity, trust, and access
  control Enablers, including identity management, authentication,
  authorisation, and trust frameworks. eGovERA documents concrete
  realisations of this pattern through reusable solutions enabling
  federated identity, single sign-on, and attribute exchange across
  administrations.

- **Cross-Domain Data Exchange.** This pattern supports the controlled
  exchange of data between heterogeneous systems and organisations (e.g.
  European Commission institutions and systems, Members States, etc). It
  builds on Enablers related to interoperability interfaces, messaging,
  data transformation, and governance. eGovERA solutions realising this
  pattern include data exchange infrastructures, interoperability
  platforms, and common service layers facilitating secure and
  standard-based data sharing.

- **Data Spaces and Data Sharing Ecosystems.** Data space patterns
  address multi-stakeholder data sharing scenarios based on common
  governance, semantic alignment, and technical interoperability. EIRA
  captures these through Enablers related to data governance, metadata
  management, semantic assets, and trust services. eGovERA documents
  operational data space solutions that realise these Enablers in
  specific policy contexts.

As already mentioned, these are a few examples that the reference
architectures are covering, but a wider range is covered within the
models. The ultimate value is provide a structured path from
architectural intent to deployable solutions while maintaining
technology neutrality.

The Domain Specific Reference Architectures: Health, Customs, and Tax
---------------------------------------------------------------------

In addition to the cross-cutting interoperability patterns, eGovERA
extending EIRA supports domain-specific solution development, which
implies domain-specific legal, organisational, and operational
constraints. To address this, a set of sectoral use cases are provided
to illustrate how the Reference Architectures are applied in concrete
policy domains.

eGovERA Health Reference Architecture [5]_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The health use case addresses highly sensitive data exchange scenarios,
including patient identification, electronic health records, and
cross-border healthcare services. It illustrates the application of EIRA
Enablers related to data protection, consent management, semantic
interoperability, and trust. This use case shows how interoperability
can be achieved while respecting strict legal and ethical requirements,
and how common architectural patterns support continuity of care across
organisational and national boundaries.

eGovERA Customs Reference Architecture [6]_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The customs use case focuses on interoperability between customs
authorities, economic operators, and other border management agencies.
It demonstrates how EIRA supports complex, multi-actor processes such as
goods declaration, risk analysis, and information sharing across
jurisdictions.

eGovERA Tax Reference Architecture [7]_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The taxation use case focuses on interoperability scenarios such as
cross-border information exchange, taxpayer identification, and
coordination between tax authorities. It demonstrates how common
architectural elements—such as identity management, secure data
exchange, and semantic alignment of fiscal data—are combined to support
compliance, transparency, and efficiency. The use case highlights how
shared Enablers enable interoperability while allowing national
administrations to retain autonomy over internal systems.

Case studies, the Reference Architectures in use
------------------------------------------------

There are different cases where EIRA and eGovERA have been used by
public administrations to analyse and design solution (digital public
services) interoperable by design and tailored to cover the specific
needs and requirements of each of their use cases.

eGovERA© success story on a Data Space and Linked Data in Flanders [8]_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DG DIGIT helped the Flemish agency for Home Affairs design a Solution
Architecture Template for “Locally Taxed”, a data space reusing local
tax decisions from over 3.000 local governments within the Flemish
region to power citizen advisory services, producing analysis and a
partial solution designs models in ArchiMate. Key success factors were
clear milestones, a multidisciplinary team, and alignment with EU goals.
The models and methods provide reusable insights for the future Smart
City/Data Space work and stakeholder-ready templates.

eGovERA success on a Data Space with the Council of Madrid [9]_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DG DIGIT supported Madrid’s Smart Urban Spaces - specifically
MercaMadrid - by creating an eGovERA-based SAT and partial solution
model to ensure interoperability across IoT-driven services
(environment, waste, lighting) via a data space, with outputs in
ArchiMate for reuse. Benefits include a scalable template to document
smart spaces, guide future tenders, and enable replicability,
cybersecurity, and digital-twin/open data integration. Success factors
were knowledge dissemination and a model adaptable to other spaces;
initial complexity was offset by ensuring interoperable exchange between
the city and providers.

eGovERA success on ViDA e invoicing requirements with DG TAXUD [10]_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Under Fiscalis FPG/042, DG TAXUD and DG DIGIT used eGovERA’s Tax
Reference Architecture to produce SAT models for “B2B intra community
transactions e Invoicing reporting,” centralizing requirements to
support Member States implementing ViDA e invoicing. The group (nine
countries) highlighted clear onboarding, blended sessions, and alignment
with EIF as key success factors. While benefits must be proven
nationally and local adaptation is pending, the approach promotes
standardization, cross border alignment, and reuse; more eGovERA
centered use cases are encouraged to address change resistance and
demonstrate impact.

First public procurement use case for EIRA and ITB with CACSA [11]_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Valencia’s CACSA applied EIRA and the Interoperability Test Bed across a
full public procurement for a new “Sede Electrónica,” using EIRA to
structure technical specifications and ITB for quality control. This
aligned procurement with EIF, expressing capabilities as Architecture
Building Blocks to ease evaluation and ensure interoperability from
requirements to award and post award activities. The case demonstrates
how EIRA+ITB can improve specification clarity, comparability, and
assurance, offering a replicable blueprint for other public
administrations seeking interoperable, cross border ready digital public
services

References
----------

.. [5] eGovernment European Reference Architecture Health Domain. See appendices for domain-specific reference architecture documentation.

.. [6] eGovernment European Reference Architecture Customs Domain. See appendices for domain-specific reference architecture documentation.

.. [7] eGovernment European Reference Architecture Tax Domain. See appendices for domain-specific reference architecture documentation.

.. [8] European Commission, DG DIGIT. Flanders Data Space Case Study: Locally Taxed Initiative. Available in the appendices and case study collection.

.. [9] European Commission, DG DIGIT. Madrid Smart Urban Spaces Case Study. Available in the appendices and case study collection.

.. [10] European Commission, DG TAXUD and DG DIGIT. ViDA e-Invoicing Reference Architecture Case Study under Fiscalis Framework. Available in the appendices.

.. [11] European Commission. CACSA Valencia Public Procurement Case Study: EIRA and Interoperability Test Bed Application. Available in the appendices and best practices documentation.