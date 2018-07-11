class Hello
  def Hello.hello()
    for i in 0..3
      puts "Hello Ruby! * #{i}"
    end
  end
end

Hello.hello()

def hello_test
  yield
end

hello_test {puts "Hello world"}

class Customer
  @@no_of_customers = 0

  def initialize(id, name, addr)
    @cust_id = id
    @cust_name = name
    @cust_addr = addr
  end

  def display_details()
    puts "Customer id #@cust_id"
    puts "Customer name #@cust_name"
    puts "Customer address #@cust_addr"
  end

  def total_no_of_customers()
    @@no_of_customers += 1
    puts "Total number of customers: #@@no_of_customers"
  end
end

# 创建对象
cust1 = Customer.new("1", "John", "Wisdom Apartments, Ludhiya")
cust2 = Customer.new("2", "Poul", "New Empire road, Khandala")

# 调用方法
cust1.display_details()
cust1.total_no_of_customers()
cust2.display_details()
cust2.total_no_of_customers()


$global_variable = 10
class Class1
  def print_global
    puts "全局变量在 Class1 中输出为 #$global_variable"
  end
end
class Class2
  def print_global
    puts "全局变量在 Class2 中输出为 #$global_variable"
  end
end

class1obj = Class1.new
class1obj.print_global
class2obj = Class2.new
class2obj.print_global

module Helloable
  def hello
    puts "Hello World"
  end
end

class IncludeClass
  include Helloable
end

class ExtendClass
  extend Helloable
end

IncludeClass.new.hello
ExtendClass.hello

module A
  def a1
  end

  def a2
  end
end

module B
  def b1
  end

  def b2
  end
end

class Sample
  include A
  include B

  def s1
  end
end

samp = Sample.new
samp.a1
samp.a2
samp.b1
samp.b2
samp.s1