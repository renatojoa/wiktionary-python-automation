  @runSearch
  Feature: Adidas Challenge Front
    Scenario Outline: Assert definition of <searchTxt>
      Given I open: https://en.wiktionary.org/prepare by the first time
      Then I am on homepage
      Then I look up the definition of the word <searchTxt>
      Given I prepare myself to be on definition page
      Then I am on definition page of the word: <searchTxt>
      Then I check that one definition is: <expectedDefinition>
      
      Examples: searchbase
        | searchTxt | expectedDefinition                                                                              |
        | apple     | A common, round fruit produced by the tree Malus domestica, cultivated in temperate climates.   |
        | pear      | 'An edible fruit produced by the pear tree, similar to an apple but elongated towards the stem. |