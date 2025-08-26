# infocomm

Information Communication Ontology

## Overview

The Information Communication Ontology (infocomm) is an OWL 2 ontology that provides a foundational semantic framework for describing information communication events. It captures the essential components and relationships involved in any communication process, from simple text messages to complex data transmissions.

**Namespace**: `http://w3id.org/infocomm#`

## Classes

### Core Classes

#### `CommunicationEvent`

The central class representing the transport of information through space and/or time. Every communication instance is modeled as a CommunicationEvent that connects all other components.

#### `Information`

Represents that which is communicated. This includes ideas, knowledge, facts, claims, feelings, plans, and any other content that can be transmitted between parties.

#### `CommunicationParty`

An entity that participates in the communication event, either as a sender or recipient. This can represent people, organisations, devices, or software systems.

### Technical Classes

#### `Medium`

A physical or virtual entity that is altered (either temporarily or permanently) to preserve information during communication. Examples include:

- Radio waves (wireless communication)
- Coaxial cables (wired communication)
- Optical fibers
- Storage devices

#### `Format`

The way in which information is structured or encoded within a medium. This encompasses:

- Data formats (JSON, CSV, PDF)
- Character encodings (UTF-8, ASCII)
- Encoding schemes (base64)
- File formats and data structures

#### `Protocol`

A set of rules that govern how communication takes place. Examples include:

- Network protocols (TCP/IP, HTTP, SMTP)
- Communication standards (Bluetooth, SMS)
- Languages (as communication protocols)

## Object Properties

### Core Relationships

- **`transmits`**: Links a CommunicationEvent to the Information being communicated
- **`hasSender`**: Identifies the CommunicationParty that transmits the information
- **`hasRecipient`**: Identifies the CommunicationParty that receives the information

### Technical Relationships

- **`hasMedium`**: Specifies the Medium used in the communication
- **`hasFormat`**: Defines the Format used to structure the information
- **`isGovernedBy`**: Links a CommunicationEvent to the Protocol that governs it

### Inverse Properties

- **`senderOf`**: Inverse of `hasSender`
- **`recipientOf`**: Inverse of `hasRecipient`
- **`governs`**: Inverse of `isGovernedBy`

## Example Usage

The ontology can model various communication scenarios:

### Text Message Example

```turtle
:AliceInvitesBobToBirthdayParty a :CommunicationEvent ;
    :transmits :BirthdayInvitationMessage ;
    :hasSender :Alice ;
    :hasRecipient :Bob ;
    :hasMedium :RadioWaves ;
    :hasFormat :PlainText ;
    :isGovernedBy :SMSProtocol .
```

### Web Service Example

```turtle
:WeatherUpdateEvent a :CommunicationEvent ;
    :transmits :WeatherForecastUpdate ;
    :hasSender :WeatherStationService ;
    :hasRecipient :Subscriber7845 ;
    :hasMedium :FibreOpticCable ;
    :hasFormat :HTML ;
    :isGovernedBy :HTTP .
```

## Constraints

- All main classes are declared as mutually disjoint
- Most object properties are functional (single-valued)
- Domain and range restrictions ensure proper usage of relationships

## Files

- **`infocomm.owl`**: Main ontology file containing class and property definitions
- **`infocomm_example.owl`**: Example instances demonstrating the ontology usage

## Applications

This ontology can be used for:

- Modeling communication systems and networks
- Analyzing information flow in organizations
- Describing messaging and data exchange protocols
- Digital forensics and communication analysis
- Semantic interoperability in communication systems

