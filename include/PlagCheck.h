#ifndef Head_PlagCheck
#define Head_PlagCheck

#include <cstddef>

namespace PlagCheck {
	extern size_t MinRunSize;
	
	class Tokenizer;
	class Text;
	class Token;
	class ForwardRefMaker;
	
	class Lang;
	template<typename T>
	class LangBase;
	class LangCpp;
	class LangPython;

	struct Idf;

}

#endif
