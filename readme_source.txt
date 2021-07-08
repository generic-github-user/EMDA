EMDA
	Efficient Multipurpose Data Architecture
	https://imgs.xkcd.com/comics/standards.png
	EMDA is a human-readable serialization$wiki language for structured data. It draws inspiration from YAML$https://yaml.org/, OGDL$https://ogdl.org/, and similar languages that minimize extraneous syntax and decoration. The main motivations for creating a new format (ie, the goals the format aims to achieve) are:
		Very efficient, painless input and maintenance of SD by humans as a core design feature
			Emphasis on abbreviations, shorthand, and syntactical sugar
		Fluid restructuring and reformatting of text and abstract data woven into the lang's workflow
		Intuitive interfacing with scripting languages like Python$https://www.python.org/
		High flexibility and sensible pathways by which to fit the system to the needs of a particular project
	Overview
		emda is a very unrestrictive format (and in some ways borders on a non-format). It embraces the idea that languages should be descriptive and not prescriptive; in practice, this means that there are many different ways to arrange the same data, and software tools can be used to seamlessly move from one arrangement to another. It is assumed that the person writing the data knows best how it should be organized, up until the point where ambiguity could be introduced. Many languages stop short of this point, forcing the user to learn unintuitive and unnecessary formatting rules that could easily be substituted with a better parsing algorithm when a standard rep is needed.
		The general rules for formatting in emda are as follows:
			Whitespace indentation[it is recommended to use tabs (1 per level), but spaces are permissible] marks nested data and contains the general structure of information
			Excepting any special processing or formatting rules applied to the plain text, emda stores data in string format
			Aside from the above, special notation and syntax must be defined in a processor or emda file; templates and presets for commonly used ones are available but the language itself does not impose these
	Examples
		Below is a fairly minimal example of data represented in emda:
		{ex}
			cat
				has
					whiskers
					fur
					head
					1 tail
					4 legs
					2 eyes
				is an
					animal
				can be a
					pet
				can do
					walk
					run
					jump
					eat
					hunt
			bird
				has
					feathers
					2 eyes
					head
					beak
					1 tail
					2 wings
				can do
					walk
					fly
					eat
					hunt
				is an
					animal
			[hidden] export: ./example.emda
		The parser will internally convert this to a Python dictionary containing the structure of the data and relationships between entries (essentially, a directed graph). We can then construct a mapping to a reorganized tree that groups on some common property; `a.is.animal -> animal.a`. This amounts to a graph rewriting operation and is an example of a common operation used to restructure DREMDA.
		
		
		
		One interesting byproduct of emda's highly dynamic nature is that it can be used to create compact microapps that combine data storage with an interface. Consider this small calculator:
		{ex}
			Run calculation
				5 ** 7
			Previous calculations
		Here is another, a minimal notes app:
		{ex}
			Add note: 
		
		
		In fact, this readme was written in emda and used to generate a md file.
