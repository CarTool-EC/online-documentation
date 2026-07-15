Solution Building Blocks (SBBs)
===============================

This section aims explain and describe what are the Solution Building
Blocks (SBBs), which is the purpose and the relationship with other
relevant aspects such as Architecture Building Blocks or specifications.

What are Solution Building Block in the EIRA
--------------------------------------------

Solution Building Blocks represent **concrete implementation choices
that realise the capabilities** defined by Architecture Building Blocks.
In EIRA terms, an SBB is an artefact that enables the implementation of
one or more EIRA ABBs within a Digital Public Service (a Solution). SBBs
constitute the actual products, technologies selected to fulfil
architectural requirements. These can be realised in turn by standards
and specifications.

Where ABBs define requirements in technology-neutral terms, SBBs
represent specific technological and implementation decisions. For
instance, if an ABB defines the requirement for secure electronic
identification, corresponding SBBs might include specific
implementations such as eIDAS-compliant identity providers, mobile ID
solutions, or smart card authentication systems. Multiple SBBs may exist
to satisfy a single ABB, reflecting different implementation approaches,
technological choices, or contextual requirements across different
member states or policy domains.

The relationship between ABBs and SBBs enables a clear separation
between architectural requirements and implementation decisions,
supporting technology neutrality whilst providing concrete guidance for
solution delivery.

SBBs and standards or specifications 
-------------------------------------

Within the European Interoperability Reference Architecture, Solution
Building Blocks (SBBs) are architectural constructs that address
specific interoperability needs and are realised through the application
of standards and specifications. Standards and specifications themselves
are not SBBs; rather, they are normative artefacts that define rules,
structures, or agreements which SBBs rely upon.

An SBB is therefore defined in terms of a set of applicable standards
and specifications and is realised by implementing or adopting them.
This distinction ensures a clear separation between the architectural
perspective provided by EIRA and the external normative frameworks that
guide implementation choices.

In many cases, interoperability is achieved not through bespoke
technical implementations but through the adoption of commonly agreed
specifications, such as semantic models, legal frameworks, or
organisational agreements. EIRA accommodates this by allowing SBBs to be
realised through specifications.

When this happens that an SBB is realised through standards or
specifications, it represents an architectural decision to adopt, apply,
or govern those specifications in a specific context, whilst preserving
technology neutrality. Such specification-based SBBs provide a bridge
between abstract Architecture Building Blocks (ABBs) and concrete
implementations, offering actionable guidance without mandating specific
products or platforms.

- **Organisational SBBs**, which are realised through organisational
  specifications such as governance frameworks, service level
  agreements, memoranda of understanding, or collaborative arrangements.

- **Semantic SBBs**, which are realised through semantic specifications
  such as data models, vocabularies, taxonomies, metadata schemas, or
  ontologies. In these cases, the SBB represents the adoption or
  governance of a shared semantic artefact, not the artefact itself.

- **Technical SBBs**, which are realised through technical standards,
  protocols, interface definitions, API specifications, or architectural
  patterns that enable technical interoperability.

An example to support the explanations is, for instance, an ABB may
express the need for semantic interoperability in data exchange. The
corresponding SBB may define the adoption of a standardised data model
or vocabulary. The vocabulary specification itself (such as a Core
Vocabulary or an international standard) remains an external artefact,
while the SBB captures the architectural choice to use that
specification to fulfil the interoperability requirement.

The bottom line is that SBBs realising standards and specifications is
key and the cornerstone for the development of digital public services:

- It promotes **interoperability by design**, ensuring that solutions
  are built on common foundations from the outset and can interoperate
  without bespoke integration.

- It **supports technology neutrality** by clearly separating what must
  be achieved from how it is implemented, allowing public
  administrations to retain flexibility while ensuring compatibility.

SBBs as COTS, OSS or complete solutions
---------------------------------------

When Solution Building Blocks take the form of COTS products,
open-source software, or complete solutions, they represent tangible
implementations that directly provide the capabilities defined by
Architecture Building Blocks. These product-based SBBs are characterised
by their easy deployability, established feature sets, and existing
support ecosystems. Unlike specification-based SBBs that define "how to
build," product-based SBBs represent "what to deploy."

As an example, an Architecture Building Block might define the
requirement for "secure document exchange between public
administrations." The corresponding product-based SBB could be an
e-Delivery Access Point implementation (such as Domibus, an open-source
solution provided by the European Commission), a commercial secure file
transfer solution, or a complete document management system with
built-in interoperability features.

Following this logic, there are different possibilities for the
selection and implementation of these SBBs:

- **Commercial Off-The-Shelf (COTS) Solutions:** Proprietary software
  products developed and maintained by commercial vendors, licensed for
  use by public administrations. COTS solutions typically offer
  comprehensive functionality, vendor support, regular updates, and
  established deployment practices. Examples include enterprise service
  bus platforms, identity management systems, or document management
  solutions that incorporate European interoperability standards.

- **Open-Source Software (OSS):** Software solutions with publicly
  available source code, licensed under open-source licences that permit
  use, modification, and redistribution. OSS solutions offer
  transparency, flexibility for customisation, community-driven
  development, and typically lower licensing costs. Examples include the
  CEF Building Blocks (such as eDelivery, eSignature, and eID), Apache
  middleware components, or open-source content management systems
  adapted for public administration use.

- **Hybrid Solutions:** Products that combine open-source core
  components with commercial extensions, support arrangements, or
  managed service offerings. These solutions balance the transparency
  and flexibility of OSS with the structured support and additional
  features of commercial products.

- **Complete Integrated Solutions:** Comprehensive platforms or suites
  that address multiple Architecture Building Blocks simultaneously,
  providing end-to-end functionality for specific use cases. Examples
  include integrated e-government platforms, cross-border service
  delivery systems, or domain-specific solutions for areas like
  e-procurement, health information exchange, or social security
  coordination.