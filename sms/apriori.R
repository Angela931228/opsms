library(arules)
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
calAll<- function(){
    rules<-apriori(data=Groceries[1:dataLength], parameter=list(supp=0.001,conf = 0.8,minlen=1))
    #inspect(rules[1:5])
    rules<-sort(rules, by="confidence", decreasing=TRUE)
    
    subset.matrix <- is.subset(rules, rules)
    subset.matrix[lower.tri(subset.matrix, diag=T)] <- NA
    redundant <- colSums(subset.matrix, na.rm=T) >= 1
    rules.pruned <- rules[!redundant]
    rules<-rules.pruned
    data.frame(inspect(rules[1:5]))
    ruledf = data.frame(lhs = labels(lhs(rules)),rhs = labels(rhs(rules)),rules@quality)
    ruledf[,c(3,4,5)] = round(ruledf[,c(3,4,5)],digits = 4)
    write.csv(ruledf,"./sms/static/sms/data/ruledf.csv", row.names = FALSE)
}

calLeft<-function(){
    rules<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
                   appearance = list(default="rhs",lhs="domestic eggs"),
                   control = list(verbose=F))
    rules<-sort(rules, decreasing=TRUE,by="confidence")
    
    subset.matrix <- is.subset(rules, rules)
    subset.matrix[lower.tri(subset.matrix, diag=T)] <- NA
    redundant <- colSums(subset.matrix, na.rm=T) >= 1
    rules.pruned <- rules[!redundant]
    rules<-rules.pruned
    data.frame(inspect(rules[1:5]))
    ruledf = data.frame(lhs = labels(lhs(rules)),rhs = labels(rhs(rules)),rules@quality)
    ruledf[,c(3,4,5)] = round(ruledf[,c(3,4,5)],digits = 4)
    write.csv(ruledf,"./sms/static/sms/data/ruledf1.csv", row.names = FALSE)
}

calRight<-function(){
    rules<-apriori(data=Groceries[1:dataLength], parameter=list(supp=0.001,conf = 0.8,minlen=2), 
                   appearance = list(default="lhs",rhs="whole milk"),
                   control = list(verbose=F))
    rules<-sort(rules, decreasing=TRUE,by="confidence")
    subset.matrix <- is.subset(rules, rules)
    subset.matrix[lower.tri(subset.matrix, diag=T)] <- NA
    redundant <- colSums(subset.matrix, na.rm=T) >= 1
    rules.pruned <- rules[!redundant]
    rules<-rules.pruned
    ruledf = data.frame(lhs = labels(lhs(rules)),rhs = labels(rhs(rules)),rules@quality)
    ruledf[,c(3,4,5)] = round(ruledf[,c(3,4,5)],digits = 4)
    write.csv(ruledf,"./sms/static/sms/data/ruledf2.csv", row.names = FALSE)
}
if(m==1){
    calAll()
}else if(m==2){
    calLeft()
}else if(m==3){
    calRight()
}else{
    calAll()
    calLeft()
    calRight()
}



