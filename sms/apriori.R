library(arules)
library(arulesViz)
library(datasets)

args = commandArgs(trailingOnly=TRUE)
options(digits=2)

m = args[1]
sp = args[2]
cf  = args[3]
dataLength = args[4]
l = args[5]
r = args[6]
# Load the data set
data(Groceries)

if(m==1){
  rules <- apriori(Groceries[1:dataLength], parameter = list(supp = 0.001, conf = 0.8))
  #inspect(rules[1:5])
  rules<-sort(rules, by="confidence", decreasing=TRUE)
  
  subset.matrix <- is.subset(rules, rules)
  subset.matrix[lower.tri(subset.matrix, diag=T)] <- NA
  redundant <- colSums(subset.matrix, na.rm=T) >= 1
  rules.pruned <- rules[!redundant]
  rules<-rules.pruned
  #inspect(rules[1:5])
  data.frame(inspect(rules))
}else if(m==2){
  rules<-apriori(data=Groceries[1:dataLength], parameter=list(supp=0.001,conf = 0.08), 
                 appearance = list(default="lhs",rhs="whole milk"),
                 control = list(verbose=F))
  rules<-sort(rules, decreasing=TRUE,by="confidence")
  subset.matrix <- is.subset(rules, rules)
  subset.matrix[lower.tri(subset.matrix, diag=T)] <- NA
  redundant <- colSums(subset.matrix, na.rm=T) >= 1
  rules.pruned <- rules[!redundant]
  rules<-rules.pruned
  data.frame(inspect(rules))
}else if(m==3){
  rules<-apriori(data=Groceries[1:dataLength], parameter=list(supp=0.001,conf = 0.15,minlen=2), 
                 appearance = list(default="rhs",lhs="whole milk"),
                 control = list(verbose=F))
  rules<-sort(rules, decreasing=TRUE,by="confidence")
  subset.matrix <- is.subset(rules, rules)
  subset.matrix[lower.tri(subset.matrix, diag=T)] <- NA
  redundant <- colSums(subset.matrix, na.rm=T) >= 1
  rules.pruned <- rules[!redundant]
  rules<-rules.pruned
  data.frame(inspect(rules))
  #inspect(rules[1:5])
}

