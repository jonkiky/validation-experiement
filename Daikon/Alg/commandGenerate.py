from subprocess import call
arry = ["cn.tf.bean.CartItemTest",
"cn.tf.bean.CartTest",
"cn.tf.commons.PageTest",
"cn.tf.controller.ClientServletTest",
"cn.tf.controller.LoginServletTest",
"cn.tf.controller.ManageServletTest",
"cn.tf.controller.PayServletTest",
"cn.tf.controller.ResponsePayServletTest",
"cn.tf.dao.BookDaoTest",
"cn.tf.dao.CategoryDaoTest",
"cn.tf.dao.OrderDaoTest",
"cn.tf.dao.PrivilegeDaoTest",
"cn.tf.dao.impl.BookDaoImplTest",
"cn.tf.dao.impl.CategoryDaoImplTest",
"cn.tf.dao.impl.CustomerDaoImplTest",
"cn.tf.dao.impl.OrderDaoImplTest",
"cn.tf.dao.impl.PrivilegeDaoImplTest",
"cn.tf.filter.CharseEncodingFilterTest",
"cn.tf.filter.GetHttpServletRequestTest",
"cn.tf.filter.PrivilegeFilterTest",
"cn.tf.service.BusinessServiceTest",
"cn.tf.service.PrivilegeServiceTest",
"cn.tf.service.impl.BusinessServiceImplTest",
"cn.tf.service.impl.PrivilegeServiceImplTest",
"cn.tf.utils.C3P0UtilTest",
"cn.tf.utils.ConstantTest",
"cn.tf.utils.OrderNumUtilTest",
"cn.tf.utils.PaymentUtilTest",
"cn.tf.utils.SendMailThreadTest",
"cn.tf.utils.WebUtilTest"]
import os
for name in arry:
    baseCommand = "java  -Xmx4g -cp"
    baseCommand = baseCommand +" F:/experiment20170325Regression/BookStore-master2/WebRoot/WEB-INF/lib/*;"
    baseCommand = baseCommand +"F:/experiment20170325Regression/BookStore-master2/target/classes/;"
    baseCommand = baseCommand +"F:/experiment20170325Regression/BookStore-master2Test/bin;"
    baseCommand = baseCommand +" daikon.Chicory   --ppt-select-pattern=\"cn.tf\" --dtrace-file=\""+name[name.rindex(".")+1:len(name)]+".dtrace.gz\" "
    baseCommand = baseCommand +name
    baseCommand = baseCommand +"&&java  -Xmx4g -cp F:/experiment20170325Regression/commons-lang-2.1.a/lib/daikon.jar; daikon.Daikon " +name[name.rindex(".")+1:len(name)]+".dtrace.gz"
    baseCommand = baseCommand +"&&java  -Xmx4g -cp F:/experiment20170325Regression/commons-lang-2.1.a/lib/daikon.jar; daikon.PrintInvariants  "+name[name.rindex(".")+1:len(name)]+".inv.gz>>"
    baseCommand = baseCommand +name[name.rindex(".")+1:len(name)]+".txt"
    #print "\n"
    #print baseCommand
    #os.system(baseCommand)







arry2 =["org.apache.commons.lang.daikon.AbstractNestableTestCase",
"org.apache.commons.lang.daikon.AbstractRangeTest",
"org.apache.commons.lang.daikon.ArrayUtilsAddTest",
"org.apache.commons.lang.daikon.ArrayUtilsRemoveTest",
"org.apache.commons.lang.daikon.ArrayUtilsTest",
"org.apache.commons.lang.daikon.BitFieldTest",
"org.apache.commons.lang.daikon.BooleanUtilsTest",
"org.apache.commons.lang.daikon.CharEncodingTest",
"org.apache.commons.lang.daikon.CharRangeTest",
"org.apache.commons.lang.daikon.CharSetTest",
"org.apache.commons.lang.daikon.CharSetUtilsTest",
"org.apache.commons.lang.daikon.CharUtilsPerfTest",
"org.apache.commons.lang.daikon.CharUtilsTest",
"org.apache.commons.lang.daikon.ClassUtilsTest",
"org.apache.commons.lang.daikon.CompareToBuilderTest",
"org.apache.commons.lang.daikon.DateFormatUtilsTest",
"org.apache.commons.lang.daikon.DateUtilsTest",
"org.apache.commons.lang.daikon.DefaultToStringStyleTest",
"org.apache.commons.lang.daikon.DoubleRangeTest",
"org.apache.commons.lang.daikon.DurationFormatUtilsTest",
"org.apache.commons.lang.daikon.EntitiesPerformanceTest",
"org.apache.commons.lang.daikon.EntitiesTest",
"org.apache.commons.lang.daikon.EnumTestSuite",
"org.apache.commons.lang.daikon.EnumUtilsTest",
"org.apache.commons.lang.daikon.EqualsBuilderTest",
"org.apache.commons.lang.daikon.ExceptionTestSuite",
"org.apache.commons.lang.daikon.ExceptionUtilsTestCase",
"org.apache.commons.lang.daikon.FastDateFormatTest",
"org.apache.commons.lang.daikon.FloatRangeTest",
"org.apache.commons.lang.daikon.FractionTest",
"org.apache.commons.lang.daikon.HashCodeBuilderAndEqualsBuilderTest",
"org.apache.commons.lang.daikon.HashCodeBuilderTest",
"org.apache.commons.lang.daikon.IllegalClassExceptionTest",
"org.apache.commons.lang.daikon.IncompleteArgumentExceptionTest",
"org.apache.commons.lang.daikon.IntRangeTest",
"org.apache.commons.lang.daikon.LangTestSuite",
"org.apache.commons.lang.daikon.LongRangeTest",
"org.apache.commons.lang.daikon.MathTestSuite",
"org.apache.commons.lang.daikon.MultiLineToStringStyleTest",
"org.apache.commons.lang.daikon.MutableByteTest",
"org.apache.commons.lang.daikon.MutableDoubleTest",
"org.apache.commons.lang.daikon.MutableFloatTest",
"org.apache.commons.lang.daikon.MutableIntTest",
"org.apache.commons.lang.daikon.MutableLongTest",
"org.apache.commons.lang.daikon.MutableObjectTest",
"org.apache.commons.lang.daikon.MutableShortTest",
"org.apache.commons.lang.daikon.MutableTestSuite",
"org.apache.commons.lang.daikon.NestableDelegateTestCase",
"org.apache.commons.lang.daikon.NestableErrorTestCase",
"org.apache.commons.lang.daikon.NestableExceptionTestCase",
"org.apache.commons.lang.daikon.NestableRuntimeExceptionTestCase",
"org.apache.commons.lang.daikon.NoFieldNamesToStringStyleTest",
"org.apache.commons.lang.daikon.NotImplementedExceptionTest",
"org.apache.commons.lang.daikon.NullArgumentExceptionTest",
"org.apache.commons.lang.daikon.NumberRangeTest",
"org.apache.commons.lang.daikon.NumberUtilsTest",
"org.apache.commons.lang.daikon.ObjectUtilsTest",
"org.apache.commons.lang.daikon.RandomStringUtilsTest",
"org.apache.commons.lang.daikon.RandomUtilsTest",
"org.apache.commons.lang.daikon.SerializationUtilsTest",
"org.apache.commons.lang.daikon.ShortPrefixToStringStyleTest",
"org.apache.commons.lang.daikon.SimpleToStringStyleTest",
"org.apache.commons.lang.daikon.StandardToStringStyleTest",
"org.apache.commons.lang.daikon.StopWatchTest",
"org.apache.commons.lang.daikon.StringEscapeUtilsTest",
"org.apache.commons.lang.daikon.StringUtilsEqualsIndexOfTest",
"org.apache.commons.lang.daikon.StringUtilsIsTest",
"org.apache.commons.lang.daikon.StringUtilsSubstringTest",
"org.apache.commons.lang.daikon.StringUtilsTest",
"org.apache.commons.lang.daikon.StringUtilsTrimEmptyTest",
"org.apache.commons.lang.daikon.SystemUtilsTest",
"org.apache.commons.lang.daikon.ToStringBuilderTest",
"org.apache.commons.lang.daikon.ToStringStyleTest",
"org.apache.commons.lang.daikon.UnhandledExceptionTest",
"org.apache.commons.lang.daikon.ValidateTest",
"org.apache.commons.lang.daikon.ValuedEnumTest",
"org.apache.commons.lang.daikon.WordUtilsTest"]









for name in arry2:
    baseCommand = "java  -Xmx4g -cp"
    baseCommand = baseCommand +" F:/experiment20170325Regression/commons-lang-2.1-src/commons-lang-2.1/lib/*;"
    baseCommand = baseCommand +"F:/experiment20170325Regression/commons-lang-2.1.c/target/classes/;"
    baseCommand = baseCommand +"F:/experiment20170325Regression/commons-lang-2.1.c/bin;"
    baseCommand = baseCommand +" daikon.Chicory   --ppt-select-pattern=\"org.apache.commons.lang\" --dtrace-file=\""+name[name.rindex(".")+1:len(name)]+".dtrace.gz\" "
    baseCommand = baseCommand +name
    baseCommand = baseCommand +"&&java  -Xmx4g -cp F:/experiment20170325Regression/commons-lang-2.1.a/lib/daikon.jar; daikon.Daikon " +name[name.rindex(".")+1:len(name)]+".dtrace.gz"
    baseCommand = baseCommand +"&&java  -Xmx4g -cp F:/experiment20170325Regression/commons-lang-2.1.a/lib/daikon.jar; daikon.PrintInvariants  "+name[name.rindex(".")+1:len(name)]+".inv.gz>>"
    baseCommand = baseCommand +name[name.rindex(".")+1:len(name)]+".txt"
    print "\n"
    print baseCommand
    #os.system(baseCommand)
#
# "org.apache.commons.collections4.daikon.AbstractArrayListTest",
# "org.apache.commons.collections4.daikon.AbstractBagTest",
# "org.apache.commons.collections4.daikon.AbstractBidiMapTest",
# "org.apache.commons.collections4.daikon.AbstractCollectionTest",
# "org.apache.commons.collections4.daikon.AbstractComparatorTest",
# "org.apache.commons.collections4.daikon.AbstractIterableMapTest",
# "org.apache.commons.collections4.daikon.AbstractIteratorTest",
# "org.apache.commons.collections4.daikon.AbstractLinkedListTest",
# "org.apache.commons.collections4.daikon.AbstractListIteratorTest",
# "org.apache.commons.collections4.daikon.AbstractListTest",
# "org.apache.commons.collections4.daikon.AbstractMapEntryTest",
# "org.apache.commons.collections4.daikon.AbstractMapIteratorTest",
# "org.apache.commons.collections4.daikon.AbstractMapTest",
# "org.apache.commons.collections4.daikon.AbstractNullComparatorTest",
# "org.apache.commons.collections4.daikon.AbstractObjectTest",
# "org.apache.commons.collections4.daikon.AbstractOrderedBidiMapDecoratorTest",
# "org.apache.commons.collections4.daikon.AbstractOrderedBidiMapTest",
# "org.apache.commons.collections4.daikon.AbstractOrderedMapIteratorTest",
# "org.apache.commons.collections4.daikon.AbstractOrderedMapTest",
# "org.apache.commons.collections4.daikon.AbstractQueueTest",
# "org.apache.commons.collections4.daikon.AbstractSetTest",
# "org.apache.commons.collections4.daikon.AbstractSortedBagTest",
# "org.apache.commons.collections4.daikon.AbstractSortedBidiMapTest",
# "org.apache.commons.collections4.daikon.AbstractSortedMapTest",
# "org.apache.commons.collections4.daikon.AbstractSortedSetTest",
# "org.apache.commons.collections4.daikon.AbstractTreeMapTest",
# "org.apache.commons.collections4.daikon.ArrayIterator2Test",
# "org.apache.commons.collections4.daikon.ArrayIteratorTest",
# "org.apache.commons.collections4.daikon.ArrayListIterator2Test",
# "org.apache.commons.collections4.daikon.ArrayListIteratorTest",
# "org.apache.commons.collections4.daikon.ArrayStackTest",
# "org.apache.commons.collections4.daikon.BagUtilsTest",
# "org.apache.commons.collections4.daikon.BooleanComparatorTest",
# "org.apache.commons.collections4.daikon.BulkTest",
# "org.apache.commons.collections4.daikon.CaseInsensitiveMapTest",
# "org.apache.commons.collections4.daikon.CircularFifoQueueTest",
# "org.apache.commons.collections4.daikon.ClosureUtilsTest",
# "org.apache.commons.collections4.daikon.CollatingIteratorTest",
# "org.apache.commons.collections4.daikon.CollectionBagTest",
# "org.apache.commons.collections4.daikon.CollectionSortedBagTest",
# "org.apache.commons.collections4.daikon.ComparableComparatorTest",
# "org.apache.commons.collections4.daikon.ComparatorChainTest",
# "org.apache.commons.collections4.daikon.CompositeCollectionTest",
# "org.apache.commons.collections4.daikon.CompositeMapTest",
# "org.apache.commons.collections4.daikon.CompositeSetTest",
# "org.apache.commons.collections4.daikon.CursorableLinkedListTest",
# "org.apache.commons.collections4.daikon.DefaultedMapTest",
# "org.apache.commons.collections4.daikon.DefaultKeyValueTest",
# "org.apache.commons.collections4.daikon.DefaultMapEntryTest",
# "org.apache.commons.collections4.daikon.DualHashBidiMapTest",
# "org.apache.commons.collections4.daikon.DualLinkedHashBidiMapTest",
# "org.apache.commons.collections4.daikon.DualTreeBidiMap2Test",
# "org.apache.commons.collections4.daikon.DualTreeBidiMapTest",
# "org.apache.commons.collections4.daikon.EnumerationUtilsTest",
# "org.apache.commons.collections4.daikon.FactoryUtilsTest",
# "org.apache.commons.collections4.daikon.FilterIteratorTest",
# "org.apache.commons.collections4.daikon.FilterListIteratorTest",
# "org.apache.commons.collections4.daikon.FixedOrderComparatorTest",
# "org.apache.commons.collections4.daikon.FixedSizeListTest",
# "org.apache.commons.collections4.daikon.FixedSizeMapTest",
# "org.apache.commons.collections4.daikon.FixedSizeSortedMapTest",
# "org.apache.commons.collections4.daikon.Flat3MapTest",
# "org.apache.commons.collections4.daikon.GrowthListTest",
# "org.apache.commons.collections4.daikon.HashBagTest",
# "org.apache.commons.collections4.daikon.HashedMapTest",
# "org.apache.commons.collections4.daikon.IndexedCollectionTest",
# "org.apache.commons.collections4.daikon.IteratorChainTest",
# "org.apache.commons.collections4.daikon.IteratorEnumerationTest",
# "org.apache.commons.collections4.daikon.IteratorIterableTest",
# "org.apache.commons.collections4.daikon.IteratorUtilsTest",
# "org.apache.commons.collections4.daikon.LazyIteratorChainTest",
# "org.apache.commons.collections4.daikon.LazyMapTest",
# "org.apache.commons.collections4.daikon.LazySortedMapTest",
# "org.apache.commons.collections4.daikon.LinkedMapTest",
# "org.apache.commons.collections4.daikon.ListIteratorWrapper2Test",
# "org.apache.commons.collections4.daikon.ListIteratorWrapperTest",
# "org.apache.commons.collections4.daikon.ListOrderedMap2Test",
# "org.apache.commons.collections4.daikon.ListOrderedMapTest",
# "org.apache.commons.collections4.daikon.ListOrderedSet2Test",
# "org.apache.commons.collections4.daikon.ListOrderedSetTest",

arry2 =[
"org.apache.commons.collections4.daikon.ListUtilsTest",
"org.apache.commons.collections4.daikon.LoopingIteratorTest",
"org.apache.commons.collections4.daikon.LoopingListIteratorTest",
"org.apache.commons.collections4.daikon.LRUMapTest",
"org.apache.commons.collections4.daikon.MapBackedSet2Test",
"org.apache.commons.collections4.daikon.MapBackedSetTest",
"org.apache.commons.collections4.daikon.MapUtilsTest",
"org.apache.commons.collections4.daikon.MultiKeyMapTest",
"org.apache.commons.collections4.daikon.MultiKeyTest",
"org.apache.commons.collections4.daikon.MultiValueMapTest",
"org.apache.commons.collections4.daikon.NodeCachingLinkedListTest",
"org.apache.commons.collections4.daikon.NodeListIteratorTest",
"org.apache.commons.collections4.daikon.ObjectArrayIteratorTest",
"org.apache.commons.collections4.daikon.ObjectArrayListIterator2Test",
"org.apache.commons.collections4.daikon.ObjectArrayListIteratorTest",
"org.apache.commons.collections4.daikon.ObjectGraphIteratorTest",
"org.apache.commons.collections4.daikon.PassiveExpiringMapTest",
"org.apache.commons.collections4.daikon.PatriciaTrie2Test",
"org.apache.commons.collections4.daikon.PatriciaTrieTest",
"org.apache.commons.collections4.daikon.PeekingIteratorTest",
"org.apache.commons.collections4.daikon.PermutationIteratorTest",
"org.apache.commons.collections4.daikon.PredicatedBagTest",
"org.apache.commons.collections4.daikon.PredicatedCollectionTest",
"org.apache.commons.collections4.daikon.PredicatedListTest",
"org.apache.commons.collections4.daikon.PredicatedMapTest",
"org.apache.commons.collections4.daikon.PredicatedQueueTest",
"org.apache.commons.collections4.daikon.PredicatedSetTest",
"org.apache.commons.collections4.daikon.PredicatedSortedBagTest",
"org.apache.commons.collections4.daikon.PredicatedSortedMapTest",
"org.apache.commons.collections4.daikon.PredicatedSortedSetTest",
"org.apache.commons.collections4.daikon.PushbackIteratorTest",
"org.apache.commons.collections4.daikon.QueueUtilsTest",
"org.apache.commons.collections4.daikon.ReferenceIdentityMapTest",
"org.apache.commons.collections4.daikon.ReferenceMapTest",
"org.apache.commons.collections4.daikon.ReverseComparatorTest",
"org.apache.commons.collections4.daikon.ReverseListIteratorTest",
"org.apache.commons.collections4.daikon.SetUniqueListTest",
"org.apache.commons.collections4.daikon.SetUtilsTest",
"org.apache.commons.collections4.daikon.SingletonIterator2Test",
"org.apache.commons.collections4.daikon.SingletonIteratorTest",
"org.apache.commons.collections4.daikon.SingletonListIteratorTest",
"org.apache.commons.collections4.daikon.SingletonMapTest",
"org.apache.commons.collections4.daikon.SplitMapUtilsTest",
"org.apache.commons.collections4.daikon.StaticBucketMapTest",
"org.apache.commons.collections4.daikon.SynchronizedBagTest",
"org.apache.commons.collections4.daikon.SynchronizedCollectionTest",
"org.apache.commons.collections4.daikon.TiedMapEntryTest",
"org.apache.commons.collections4.daikon.TransformedBagTest",
"org.apache.commons.collections4.daikon.TransformedCollectionTest",
"org.apache.commons.collections4.daikon.TransformedListTest",
"org.apache.commons.collections4.daikon.TransformedMapTest",
"org.apache.commons.collections4.daikon.TransformedQueueTest",
"org.apache.commons.collections4.daikon.TransformedSetTest",
"org.apache.commons.collections4.daikon.TransformedSortedBagTest",
"org.apache.commons.collections4.daikon.TransformedSortedMapTest",
"org.apache.commons.collections4.daikon.TransformedSortedSetTest",
"org.apache.commons.collections4.daikon.TransformedSplitMapTest",
"org.apache.commons.collections4.daikon.TransformerUtilsTest",
"org.apache.commons.collections4.daikon.TransformingComparatorTest",
"org.apache.commons.collections4.daikon.TreeBagTest",
"org.apache.commons.collections4.daikon.TreeBidiMapTest","org.apache.commons.collections4.daikon.TreeListTest"]
arry2 =[
"org.apache.commons.collections4.daikon.TrieUtilsTest",
"org.apache.commons.collections4.daikon.UniqueFilterIteratorTest",
"org.apache.commons.collections4.daikon.UnmodifiableBagTest",
"org.apache.commons.collections4.daikon.UnmodifiableBidiMapTest",
"org.apache.commons.collections4.daikon.UnmodifiableBoundedCollectionTest",
"org.apache.commons.collections4.daikon.UnmodifiableCollectionTest",
"org.apache.commons.collections4.daikon.UnmodifiableIteratorTest",
"org.apache.commons.collections4.daikon.UnmodifiableListIteratorTest",
"org.apache.commons.collections4.daikon.UnmodifiableListTest",
"org.apache.commons.collections4.daikon.UnmodifiableMapEntryTest",
"org.apache.commons.collections4.daikon.UnmodifiableMapIteratorTest",
"org.apache.commons.collections4.daikon.UnmodifiableMapTest",
"org.apache.commons.collections4.daikon.UnmodifiableOrderedBidiMapTest",
"org.apache.commons.collections4.daikon.UnmodifiableOrderedMapIteratorTest",
"org.apache.commons.collections4.daikon.UnmodifiableOrderedMapTest",
"org.apache.commons.collections4.daikon.UnmodifiableQueueTest",
"org.apache.commons.collections4.daikon.UnmodifiableSetTest",
"org.apache.commons.collections4.daikon.UnmodifiableSortedBagTest",
"org.apache.commons.collections4.daikon.UnmodifiableSortedBidiMapTest",
"org.apache.commons.collections4.daikon.UnmodifiableSortedMapTest",
"org.apache.commons.collections4.daikon.UnmodifiableSortedSetTest",
"org.apache.commons.collections4.daikon.UnmodifiableTrieTest"]

arry2=["org.apache.commons.validator.daikon.BaseCalendarValidatorTest",
"org.apache.commons.validator.daikon.BaseNumberValidatorTest",
"org.apache.commons.validator.daikon.BigDecimalValidatorTest",
"org.apache.commons.validator.daikon.BigIntegerValidatorTest",
"org.apache.commons.validator.daikon.ByteTest",
"org.apache.commons.validator.daikon.ByteValidatorTest",
"org.apache.commons.validator.daikon.CalendarValidatorTest",
"org.apache.commons.validator.daikon.CreditCardValidatorTest",
"org.apache.commons.validator.daikon.CurrencyValidatorTest",
"org.apache.commons.validator.daikon.DateTest",
"org.apache.commons.validator.daikon.DateValidatorTest",
"org.apache.commons.validator.daikon.DoubleTest",
"org.apache.commons.validator.daikon.DoubleValidatorTest",
"org.apache.commons.validator.daikon.EmailTest",
"org.apache.commons.validator.daikon.EntityImportTest",
"org.apache.commons.validator.daikon.ExceptionTest",
"org.apache.commons.validator.daikon.ExtensionTest",
"org.apache.commons.validator.daikon.FieldTest",
"org.apache.commons.validator.daikon.FlagsTest",
"org.apache.commons.validator.daikon.FloatTest",
"org.apache.commons.validator.daikon.FloatValidatorTest",
"org.apache.commons.validator.daikon.GenericValidatorTest",
"org.apache.commons.validator.daikon.IntegerTest",
"org.apache.commons.validator.daikon.IntegerValidatorTest",
"org.apache.commons.validator.daikon.ISBNValidatorTest",
"org.apache.commons.validator.daikon.LocaleTest",
"org.apache.commons.validator.daikon.LongTest",
"org.apache.commons.validator.daikon.LongValidatorTest",
"org.apache.commons.validator.daikon.MultipleConfigFilesTest",
"org.apache.commons.validator.daikon.MultipleTests",
"org.apache.commons.validator.daikon.NameBean",
"org.apache.commons.validator.daikon.PercentValidatorTest",
"org.apache.commons.validator.daikon.RequiredIfTest",
"org.apache.commons.validator.daikon.RequiredNameTest",
"org.apache.commons.validator.daikon.RetrieveFormTest",
"org.apache.commons.validator.daikon.RoutinesTestSuite",
"org.apache.commons.validator.daikon.ShortTest",
"org.apache.commons.validator.daikon.ShortValidatorTest",
"org.apache.commons.validator.daikon.TestCommon",
"org.apache.commons.validator.daikon.TestNumber",
"org.apache.commons.validator.daikon.TestTypeValidator",
"org.apache.commons.validator.daikon.TestValidator",
"org.apache.commons.validator.daikon.TimeValidatorTest",
"org.apache.commons.validator.daikon.TypeBean",
"org.apache.commons.validator.daikon.TypeTest",
"org.apache.commons.validator.daikon.UrlTest",
"org.apache.commons.validator.daikon.ValidatorResultsTest",
"org.apache.commons.validator.daikon.ValidatorTest",
"org.apache.commons.validator.daikon.ValidatorTestSuite",
"org.apache.commons.validator.daikon.ValueBean",
"org.apache.commons.validator.daikon.VarTest"]



arry2=[
"org.apache.commons.validator.daikon.EntityImportTest",
"org.apache.commons.validator.daikon.ExceptionTest",
"org.apache.commons.validator.daikon.ExtensionTest",
"org.apache.commons.validator.daikon.FieldTest",
"org.apache.commons.validator.daikon.FlagsTest",
"org.apache.commons.validator.daikon.FloatTest",
"org.apache.commons.validator.daikon.FloatValidatorTest",
"org.apache.commons.validator.daikon.GenericValidatorTest",
"org.apache.commons.validator.daikon.IntegerTest",
"org.apache.commons.validator.daikon.IntegerValidatorTest",
"org.apache.commons.validator.daikon.ISBNValidatorTest",
"org.apache.commons.validator.daikon.LocaleTest",
"org.apache.commons.validator.daikon.LongTest",
"org.apache.commons.validator.daikon.LongValidatorTest",
"org.apache.commons.validator.daikon.MultipleConfigFilesTest",
"org.apache.commons.validator.daikon.MultipleTests",
"org.apache.commons.validator.daikon.NameBean",
"org.apache.commons.validator.daikon.PercentValidatorTest",
"org.apache.commons.validator.daikon.RequiredIfTest",
"org.apache.commons.validator.daikon.RequiredNameTest",
"org.apache.commons.validator.daikon.RetrieveFormTest",
"org.apache.commons.validator.daikon.RoutinesTestSuite",
"org.apache.commons.validator.daikon.ShortTest",
"org.apache.commons.validator.daikon.ShortValidatorTest",
"org.apache.commons.validator.daikon.TestCommon",
"org.apache.commons.validator.daikon.TestNumber",
"org.apache.commons.validator.daikon.TestTypeValidator",
"org.apache.commons.validator.daikon.TestValidator",
"org.apache.commons.validator.daikon.TimeValidatorTest",
"org.apache.commons.validator.daikon.TypeBean",
"org.apache.commons.validator.daikon.TypeTest",
"org.apache.commons.validator.daikon.UrlTest",
"org.apache.commons.validator.daikon.ValidatorResultsTest",
"org.apache.commons.validator.daikon.ValidatorTest",
"org.apache.commons.validator.daikon.ValidatorTestSuite",
"org.apache.commons.validator.daikon.ValueBean",
"org.apache.commons.validator.daikon.VarTest"]



for name in arry2:

    baseCommand = "java  -Xmx4g -cp "
    baseCommand = baseCommand +"F:/Regression2/lib/*;"
    baseCommand = baseCommand +"F:\\Regression2\\commons-validator-1.3.0-src\\bin;"
    baseCommand = baseCommand + "F:/experiment20170325Regression/commons-lang-2.1.a/lib/daikon.jar;"
    baseCommand = baseCommand +" daikon.Chicory " \
                               " --dtrace-file=\""+name[name.rindex(".")+1:len(name)]+".dtrace.gz\" "
    baseCommand = baseCommand +name
    baseCommand = baseCommand +"&&java  -Xmx4g -cp F:/experiment20170325Regression/commons-lang-2.1.a/lib/daikon.jar; daikon.Daikon " +name[name.rindex(".")+1:len(name)]+".dtrace.gz"
    baseCommand = baseCommand +"&&java  -Xmx4g -cp F:/experiment20170325Regression/commons-lang-2.1.a/lib/daikon.jar; daikon.PrintInvariants  "+name[name.rindex(".")+1:len(name)]+".inv.gz>>"
    baseCommand = baseCommand +name[name.rindex(".")+1:len(name)]+".txt"
    print "\n"
    print baseCommand
    os.system(baseCommand)











