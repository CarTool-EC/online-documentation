Introduction
============

The European public sector is undergoing a profound digital
transformation driven by increasing societal expectations, cross-border
service demands, rapid technological change, and an evolving European
regulatory landscape. Public administrations are now required to design,
implement, and operate interoperable, high-quality and trustworthy
digital public services, while ensuring compliance with EU legislation
such as the Interoperable Europe Act, the GDPR, the Open Data Directive,
the Data Governance Act, the Data Act, and domain-specific legal
frameworks.

In this context, interoperability has become a foundational capability
for modern public administrations. It enables administration-wide and
cross-border collaboration, promotes reuse of solutions and building
blocks, reduces fragmentation and vendor-lock-in, and ensures that
digital public services can work together seamlessly to deliver public
value. Interoperability is not only a technical requirement, but a
policy, organisational and semantic capability that must be built into
the full lifecycle of digital public services.

To support this effort, the European Commission, through the
Interoperable Europe initiative, provides a set of reference
architectures, methodological frameworks, and reusable resources that
guide Member States and EU institutions in the design and implementation
of interoperable solutions. Among these, two key instruments play a
central role:

- The **European Interoperability Reference Architecture (EIRA)**: it is
  a formal meta concept, level 1 granularity vocabulary of Architecture
  Building Blocks (ABBs) expressed in ArchiMate, structured along the
  Legal, Organisational, Semantic and Technical (LOST) interoperability
  views defined by the European Interoperability Framework (EIF). EIRA
  supports the analysis of a digital public service requirements use
  case and the design of a digital public service use case enabling the
  identification of reusable solution building blocks.

- The **eGovernment European Reference Architecture (eGovERA)**: it is a
  formal level 2 and further granularity vocabulary, based on and
  extending EIRA. eGovERA includes architecture patterns, and it
  supports analysis and design of a digital public service use cases.

This specification covers EIRA as the level 1 granularity of the
European Interoperability Reference Architecture and eGovERA as the
level 2 and further level of granularity of the European
Interoperability Reference Architecture. For the sake of simplification,
the term European Interoperability Reference Architecture, EIRA, covers
also eGovERA. When appropriate in this document eGovERA aspects of the
specification will be explicited. EIRA and eGovERA provide a coherent,
architecture-driven and model-based approach sypporting the
implementation life-cycle of interoperable, high-quality digital public
services.

Purpose of this Specification
-----------------------------

This specification documents the European Interoperability Reference
Architecture, eGovERA included. It provides:

- A harmonised conceptual and methodological foundation aligning EIRA
  and eGovERA.

- A clear description of the roles, use cases, and value proposition of
  each reference architecture.

- A detailed presentation of the interoperability views, building
  blocks, architecture patterns, and modelling conventions.

Guidance for conformance, governance, quality assurance, and lifecycle
management of digital public service solutions.

Scope
-----

This specification defines the European Interoperability Reference
Architecture, EIRA , and establishes a unified architectural and
methodological framework to support the analysis, design and governance
of interoperable digital public services in the European Union public
administrations.

The scope of this specification includes:

- A harmonised conceptual foundation describing the principles,
  architecture ontology, modelling conventions and interoperability
  views (Legal, Organisational, Semantic and Technical) that underpin
  the reference architectures.

- The definition and structuring of Architecture Building Blocks (ABBs)
  and their transformation into Solution Building Blocks (SBBs) to
  support the full lifecycle of digital public service engineering.

- The methodological alignment between analysis and design, including
  decomposition principles, traceability rules, architecture patterns
  and interoperability considerations.

- Guidance for role-based use of the reference architectures, enabling
  different professional profiles to navigate the models according to
  their domain concerns.

- Conformance and governance provisions, including interoperability
  assessment, model quality requirements, and architecture-driven
  decision-support for digital public service implementation.

The following aspects are outside the scope of this specification:

- Domain-specific reference architectures, although the present
  specification provides the common domain-agnostic foundation on which
  they may be based.

- Detailed implementation procedures, procurement templates and
  operational manuals.

- Tool-specific modelling instructions beyond the use of ArchiMate as
  the prescribed architecture ontology.

- Organisation-specific governance arrangements, except where directly
  required to fulfil EU-level interoperability principles.

Target Audience
---------------

This specification is designed for:

- Policy Makers & Digital Strategy Leaders.

- Enterprise & Solution Architects.

- Portfolio & Programme Managers.

- Solution Providers & Project Teams.

- Academia & Training Organisations.

Relationship to Other Frameworks and Standards
----------------------------------------------

The Reference Architecture aligns with, and draws inspiration from:

- Interoperability frameworks (e.g., EIF, national frameworks).

- Enterprise architecture methodologies (e.g., TOGAF(c)).

- Modelling standards (e.g., ArchiMate(c) ).

- Technical specifications (e.g., W3C standards for semantic and web
  interoperability).

Document Conventions and Terminology
-------------------------------------

- Normative Text: MUST, MUST NOT, SHOULD, SHOULD NOT, MAY (RFC 2119).

- Non-Normative Text: Guidance and recommendations (not binding).

- Reference Architecture (RA): A standardised architectural framework.

- Architecture Building Block (ABB): Abstract, reusable element.

- Solution Building Block (SBB): Concrete implementation of ABBs.

- Interoperability Views: Legal, Organisational, Semantic, Technical.