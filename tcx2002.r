mixed_numeric_logical <- c(1, 3, 4, TRUE)
# calling mixed_numeric_logical returns 1 3 4 1
typeof(mixed_numeric_logical) # returns "double"
class(mixed_numeric_logical) # returns "numeric"

sales_vector <- c(100, 150, 200, 120, 180, 160) # 1-D vector
sales_matrix <- matrix(sales_vector, nrow = 2, ncol = 3)
## returns:
##       [,1] [,2] [,3]
## [1,]  100  200  180
## [2,]  150  120  160

rownames(sales_matrix) <- c("Store_A", "Store_B") # add row names
colnames(sales_matrix) <- c("Q1", "Q2", "Q3") # add column names
## returns:
##          Q1  Q2  Q3
## Store_A 100 200 180
## Store_B 150 120 160

priority_vector <- c("Low", "Medium", "High", "Low", "High") # class(product_vector) = "character" class
priority_basic <- factor(priority_vector) # class(product_categories) = "factor" class
    # factor() converts vector to categorical data
## returns:
## Low    Medium High   Low    High  
## High Low Medium
levels(priority_basic) # shows unique categories
## Levels: High Low Medium
priority_with_levels <- factor(priority_vector, levels = c("Low", "Medium", "High")) # class(priority_with_levels) = "factor" class
    # with levels (custom order)
## returns:
## Low    Medium High   Low    High  
## Levels: Low Medium High
priority_ordered <- factor(priority_vector, levels = c("Low", "Medium", "High"), ordered = TRUE) # class(priority_ordered) = "ordered" "factor" class
    # with levels AND ordering (enables comparison)
## returns:
## Low    Medium High   Low    High  
## Levels: Low < Medium < High

customers <- data.frame(
  id = c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
  name = c("Alice", "Bob", "Carol", "David", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack"),
  age = c(25, 30, 35, 28, 32, 29, 27, 31, 26, 33),
  spent = c(150, 200, 300, 175, 250, 180, 220, 190, 160, 280),
  region = factor(c("North", "South", "North", "East", "West", "South", "North", "East", "West", "South"))  # Factor column
)
## returns:
##    id  name age spent region
## 1   1 Alice  25   150  North
## 2   2   Bob  30   200  South
## 3   3 Carol  35   300  North
## 4   4 David  28   175   East
## 5   5   Eve  32   250   West
## 6   6 Frank  29   180  South
## 7   7 Grace  27   220  North
## 8   8 Henry  31   190   East
## 9   9   Ivy  26   160   West
## 10 10  Jack  33   280  South

