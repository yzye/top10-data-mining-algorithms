# Assignment 1, Part 2: Simple optimization
# (gradient descent and coordinate descent)

import math
import random
import time
import losses


def gradient_descent(func_grad, init_point, step_size, num_iters):
    """ Run num_iters iterations of gradient descent.

    func_grad is the user supplied gradient.
    init_point is the initial point to start the optimization.
    step_size is the step size parameter.
    """

    curr_iter = init_point  # initialize iterate
    dim = len(init_point)  # remember dimension

    for i in range(num_iters):

        # get current gradient
        curr_gradient = func_grad(curr_iter)

        # check whether gradient is of correct dimension
        if len(curr_gradient) != dim:
            raise Exception("Expected argument func_grad to return \
                            gradient of dimension %d, got %d."
                            % (dim, len(curr_gradient)))

        # TASK 2.1.1
        # multiply gradient by step size
        scaled_gradient = [step_size * c for c in curr_gradient]

        # TASK 2.1.2
        # subtract scaled gradient from current iterate
        curr_iter = [m-n for m,n in zip(curr_iter,scaled_gradient)]

    return curr_iter


def coordinate_descent(func_grad_1d, init_point, step_size, num_iters,
                       choice='cyclic'):
    """ Run num_iters iterations of coordinate descent.

    func_grad_1d(point, j) should return the jth partial derivative at point x.
    init_point is the initial point to start the optimization.
    step_size is the step size parameter.
    choice is one of:
        'cyclic' - cycle through the coordinate
        'random' - pick coordinates at random
    """

    curr_iter = init_point  # initialize iterate
    dim = len(init_point)  # remember dimension

    for i in range(num_iters):

        # figure out coordinates to go over
        if choice == 'cyclic':
            # TASK 2.2.1
            # choose integers 0 thru dim-1
            coordinates = [m for m in range(dim)]
        elif choice == 'random':
            # TASK 2.2.2
            # choose dim random integers in {0,...,dim-1}
            # (with replacement)
            coordinates = [random.randint(0,dim-1) for n in range(dim)]
        else:
            raise Exception("Expected argument choice to be either 'cyclic' \
                            or 'random', got %s." % choice)

        # TASK 2.2.3
        # update each of the chosen coordinates
        for j in coordinates:
            curr_iter[j] = curr_iter[j] - step_size*func_grad_1d(curr_iter,j)

    return curr_iter


# TASK 2.3.1
# Complete the function definition below by replacing
# the pass statement with EXACTLY 1 line of code.
def vector_dot(u, v):
    """ Return the dot (or inner) product between u and v."""

    return sum(i*j for i, j in zip(u, v))


def loss_calculator(X, Y, scalar_loss, beta):
    """ Calculate average scalar_loss of beta on the dataset X, Y. """

    if len(X) != len(Y):
        raise Exception('Expected X and Y to be of same length.')
    else:
        n = len(Y)

    loss_sum = 0.0
    for i in range(n):
        # calculate inner product between X[i] and beta
        inner_prod = vector_dot(X[i], beta)

        loss_sum += scalar_loss(inner_prod, Y[i])

    # divide by no. of sample since we're calculating average loss
    return loss_sum/n


def loss_grad_calculator(X, Y, scalar_loss_deriv, beta):
    """ Calculate gradient of average scalar_loss of beta on the
    dataset X, Y.
    """

    if len(X) != len(Y):
        raise Exception('Expected X and Y to be of same length.')
    else:
        n = len(Y)

    dim = len(X[0])
    loss_grad_sum = dim*[0.0]
    for i in range(n):
        # calculate inner product between X[i] and beta
        inner_prod = vector_dot(X[i], beta)

        # TASK 2.3.2
        # calculate gradient (w.r.t. beta) of the loss on example i
        # (you'll need to use scalar_loss_deriv here)
        loss_grad_on_i = [scalar_loss_deriv(inner_prod, Y[i])*x for x in X[i]]

        # TASK 2.3.3
        # add loss_grad_on_i (elementwise) to the sum so far
        loss_grad_sum = [p+q for p,q in zip(loss_grad_sum,loss_grad_on_i)]

    # divide by no. of samples before returning
    return [x/n for x in loss_grad_sum]


def loss_grad_1d_calculator(X, Y, scalar_loss_deriv, beta, j):
    """ Calculate partial derivative (w.r.t. beta_j) of average scalar loss of
    beta on the data set X, Y.
    """

    if len(X) != len(Y):
        raise Exception('Expected X and Y to be of same length.')
    else:
        n = len(Y)

    loss_grad_1d_sum = 0.0
    for i in range(n):
        # calculate inner product between X[i] and beta
        inner_prod = vector_dot(X[i], beta)

        # TASK 2.3.4
        # calculate partial derivative (w.r.t. beta_j) of the loss on example i
        # (you'll need to use scalar_loss_deriv here)
        # and add it to the sum so far
        loss_grad_1d_sum += scalar_loss_deriv(inner_prod, Y[i])*X[i][j]

    # divide by no. of sample before returning
    return loss_grad_1d_sum/n


def main():

    n, d = 1000, 10  # sample size and dimension

    noise_var = 1.0  # noise variance in linear model

    # dictionary with scalar loss functions
    loss = {'squared': losses.squared_loss, 'logistic': losses.logistic_loss}

    # dictionary with derivatives of scalar loss functions
    loss_deriv = {'squared': losses.squared_loss_deriv,
                  'logistic': losses.logistic_loss_deriv}

    # choose the true parameter beta_star
    beta_star = [(10-i)/10.0 for i in range(d)]

    X = []
    Y = []

    for i in range(n):
        # new_x has standard normal entries
        new_x = [random.gauss(0, 1) for j in range(d)]

        # compute inner product between new_x and beta_star
        inner_prod = vector_dot(new_x, beta_star)

        # compute the continuous response variable
        new_y = inner_prod + random.gauss(0, math.sqrt(noise_var))

        X.append(new_x)
        Y.append(new_y)

    # TASK 2.4.1
    # create the 3 functions correctly to give to optimizers
    # use the loss and loss_deriv dictionaries here
    # along with the 3 functions: loss_calculator, loss_grad_calculator,
    # and loss_grad_1d_calculator
    squared_loss = lambda x:loss_calculator(X, Y, loss['squared'],x)
    squared_loss_grad = lambda x:loss_grad_calculator(X, Y, loss_deriv['squared'], x)
    squared_loss_grad_1d = lambda x,y:loss_grad_1d_calculator(X, Y, loss_deriv['squared'], x, y)

    print "="*80
    print "Gradient Descent Test"
    print "="*80

    init_point = d*[0.0]
    num_iters = 100
    print "Starting objective is: %f" % squared_loss(init_point)
    t0 = time.time()
    final_point = gradient_descent(squared_loss_grad, init_point,
                                   .1, num_iters)
    t1 = time.time()
    print "Objective after %d iterations of gradient descent: %f" \
        % (num_iters, squared_loss(final_point))
    print "True parameter: %s" % str(beta_star)
    print "Estimated parameter: %s" % str(final_point)
    print "Optimization took %f seconds." % (t1 - t0)

    print "="*80
    print "Coordinate Descent Test"
    print "="*80

    init_point = d*[0.0]
    num_iters = 100
    print "Starting objective is: %f" % squared_loss(init_point)
    t0 = time.time()
    final_point = coordinate_descent(squared_loss_grad_1d, init_point,
                                     .1, num_iters)
    t1 = time.time()
    print "Objective after %d iterations of coordinate descent: %f" \
        % (num_iters, squared_loss(final_point))
    print "True parameter: %s" % str(beta_star)
    print "Estimated parameter: %s" % str(final_point)
    print "Optimization took %f seconds." % (t1 - t0)

    # now create classification data set
    X = []
    Y = []
    for i in range(n):
        # new_x has standard normal entries
        new_x = [random.gauss(0, 1) for j in range(d)]

        # compute inner product between new_x and beta_star
        inner_prod = vector_dot(new_x, beta_star)

        # compute the binary response variable
        logistic = math.exp(inner_prod)/(1+math.exp(inner_prod))
        if random.random() <= logistic:
            new_y = 1
        else:
            new_y = -1

        X.append(new_x)
        Y.append(new_y)

    # TASK 2.4.2
    # create the 3 functions correctly to give to optimizers
    # use the loss and loss_deriv dictionaries here
    # along with the 3 functions: loss_calculator, loss_grad_calculator,
    # and loss_grad_1d_calculator
    logistic_loss = lambda x:loss_calculator(X, Y, loss['logistic'],x)
    logistic_loss_grad = lambda x:loss_grad_calculator(X, Y, loss_deriv['logistic'], x)
    logistic_loss_grad_1d = lambda x,y:loss_grad_1d_calculator(X, Y, loss_deriv['logistic'], x, y)

    print "="*80
    print "Gradient Descent Test (logistic regression)"
    print "="*80

    init_point = d*[0.0]
    num_iters = 500
    print "Starting objective is: %f" % logistic_loss(init_point)
    t0 = time.time()
    final_point = gradient_descent(logistic_loss_grad, init_point,
                                   .1, num_iters)
    t1 = time.time()
    print "Objective after %d iterations of gradient descent: %f" \
        % (num_iters, logistic_loss(final_point))
    print "True parameter: %s" % str(beta_star)
    print "Estimated parameter: %s" % str(final_point)
    print "Optimization took %f seconds." % (t1 - t0)

    print "="*80
    print "Coordinate Descent Test (logistic regression)"
    print "="*80

    init_point = d*[0.0]
    num_iters = 500
    print "Starting objective is: %f" % logistic_loss(init_point)
    t0 = time.time()
    final_point = coordinate_descent(logistic_loss_grad_1d, init_point,
                                     .1, num_iters)
    t1 = time.time()
    print "Objective after %d iterations of coordinate descent: %f" \
        % (num_iters, logistic_loss(final_point))
    print "True parameter: %s" % str(beta_star)
    print "Estimated parameter: %s" % str(final_point)
    print "Optimization took %f seconds." % (t1 - t0)


if __name__ == '__main__':
    main()
